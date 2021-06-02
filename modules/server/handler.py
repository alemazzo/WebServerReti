import http.server

from modules.requests.parser import RequestParser
from modules.response.response import Response
from modules.app import app


class Handler(http.server.BaseHTTPRequestHandler):
    """
    HTTP Request Handler
    """

    # The request parser
    parser = RequestParser()

    def send_request_to_view(self):
        """
        Handle the generic request and send it to the correct view
        """

        # Unpack the request and extract the data
        request = self.parser.parse(self)

        # Log the request
        print(request.method + " url = " + request.url + " parameters = " +
              str(request.parameters) + " data = " + str(request.data))

        # Check if the urls is valid, otherwise send a 404
        if request.url in app.routes:
            view = app.routes[request.url]
            view(request)
        else:
            response = Response(self)
            response.status_code(404)
            response.file('pages/errors/404.html')
            response.send()

    # Map each method to send_request_to_view()

    def do_GET(self):
        """
        Handle the GET requests
        """
        self.send_request_to_view()

    def do_HEAD(self):
        """
        Handle the HEAD requests
        """
        self.send_request_to_view()

    def do_POST(self):
        """
        Handle the POST requests
        """
        self.send_request_to_view()
