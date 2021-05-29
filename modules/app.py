import socketserver
import sys
import signal
import json
from base64 import b64encode

from modules.response.response import Response


class App:
    """
    Web Server Application
    Manage the HTTP Server and the routes of the application
    """

    def __init__(self):
        self.routes = {}
        self.server = None
        self.credentials = ""
        self._load_credentials()

    def _load_credentials(self):
        # Load the admin credentials from the
        # json file and encode in b64 for base auth
        with open('credentials.json') as data:
            jsondata = json.load(data)
            self.credentials = f'{jsondata["username"]}:{jsondata["password"]}'
            self.credentials = 'Basic ' + b64encode(
                self.credentials.encode()).decode("ascii")

    def method_not_allowed(self, route, method, request):
        """
        Response with Method Not Allowed.
        """
        response = Response(request)
        response.status_code(405)
        response.file('pages/errors/405.html')
        response.send()

    def authentication_required(self, request, message):
        """
        Response with the request of authentication
        """
        response = Response(request)
        response.status_code(401)
        response.headers(('WWW-Authenticate',
                          'Basic realm="Enter the admin credentials"'))
        response.file('pages/errors/401.html')
        response.send()

    def route(self, route, methods, auth=False):
        """
        This is an essential part of the application, it's used as a 
        decorator of a generic function making it a views of the
        application that respond to a specific url (route)

        It also specified the allowed methods in order to filter
        the request and return a 405 if a non valid method is requested
        at a specified route.

        Add also the authentication functionality for the single route through
        the Basic Authentication that work for a single session of the user.
        """

        def wrapper(func):

            # The wrapper of the view
            def inner(method, request, url, parameters, data=None):

                # Check the method availability
                if not method in methods:
                    return self.method_not_allowed(route, method, request)

                # Check if authentication is required
                if auth:
                    if request.headers['Authorization'] == None:
                        return self.authentication_required(request, 'No credentials sent')
                    elif request.headers['Authorization'] != self.credentials:
                        return self.authentication_required(request, 'Wrong credentials')

                # Response to the request through the specified view that now
                # had passed all the filtering and tests.
                func(method, request, url, parameters, data)

            # Add the following route to the dictionary of all the routes
            self.routes[route] = inner
        return wrapper

    def start(self, port):
        """
        Start the server
        """
        from modules.server.handler import Handler
        self.server = socketserver.ThreadingTCPServer(('', port), Handler)
        self.server.daemon_threads = True
        self.server.allow_reuse_address = True

        def signal_handler(signal, frame):
            print('Exiting http server (Ctrl+C pressed)')
            try:
                if(server):
                    server.server_close()
            finally:
                sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        try:
            while True:
                # sys.stdout.flush()
                self.server.serve_forever()
        except KeyboardInterrupt:
            pass

        self.server.server_close()


app = App()
