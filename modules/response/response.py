
class Response:
    """
    Generic response for a request.
    Give access to manage status code, headers, content type and the response data
    """

    def __init__(self, request):
        self._request = request

        self._status_code = None
        self._content_type = 'text/html'
        self._headers = []
        self._data = None

    def status_code(self, _status_code):
        """
        Set the status code for the response
        """
        self._status_code = _status_code

    def content_type(self, _content_type):
        """
        Set the content type for the response
        """
        self._content_type = _content_type

    def headers(self, *headers):
        """
        Set the headers for the response
        """
        self._headers = headers

    def file(self, path):
        """
        Set the file for the response
        """
        with open(path, 'rb') as file:
            self._data = file.read()

    def raw(self, data: bytes):
        """
        Set the raw data for the response
        """
        self._data = data

    def _send_headers(self):
        self._request.send_response(self._status_code)
        self._request.send_header('Content-type', self._content_type)
        for header in self._headers:
            self._request.send_header(header[0], header[1])
        self._request.end_headers()

    def send(self):
        """
        Send the response
        """
        self._send_headers()
        self._request.wfile.write(self._data)
