
class Request:
    """
    Generic data structure for handling a request
    """

    def __init__(self, connection, method, url, parameters, data=None):
        self.connection = connection
        self.method = method
        self.url = url
        self.parameters = parameters
        self.data = data
