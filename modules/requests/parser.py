import json

from modules.requests.methods import Methods


class RequestParser:
    """
    Parse the request in order to get:
        - method
        - url
        - parameters
        - post data
    """

    def _parse_parameters(self, path):
        url = path
        parameters = {}

        # Check if there are get parameters
        if '?' in path:
            url, params = path.split('?')

            # Check if there are multiple parameters
            if '&' in params:
                params = params.split('&')
            else:
                params = [params]

            # Build the parameters's dictionary
            for param in params:
                name, value = None, None
                if '=' in param:
                    name, value = param.split('=')
                else:
                    name = param
                parameters.update({name: value})

        return url, parameters

    def _parse_post_data(self, request):
        """
        Unpack the post data (if present)
        """

        data = None

        # Check if it's a POST request
        if request.command == Methods.POST:

            # Try to load the json data from the request.
            # Only data form accepted is JSON
            try:
                content_len = int(request.headers['content-length'])
                data = json.loads(request.rfile.read(content_len).decode())
            except:
                pass
        return data

    def parse(self, request):
        """
        Unpack the request
        """
        method = request.command
        url, parameters = self._parse_parameters(request.path)
        data = self._parse_post_data(request)

        return method, url, parameters, data
