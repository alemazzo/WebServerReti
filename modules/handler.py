import http.server

from modules.requests.parser import RequestParser
from modules.urls import urls_map


class Handler(http.server.BaseHTTPRequestHandler):

    parser = RequestParser()

    def send_request_to_view(self):
        """
        Handle the generic request and send it to the correct view
        """

        # Unpack the request and extract the data
        method, url, parameters, data = self.parser.parse(self)

        # Log the request
        print(method + " url = " + url + " parameters = " +
              str(parameters) + " data = " + str(data))

        # Check if the urls is valid, otherwise send a 404
        if url in urls_map:
            view = urls_map[url]
            view(method, self, url, parameters, data)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('404 - Not Found', "utf8"))

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
