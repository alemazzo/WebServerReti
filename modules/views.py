import json
from base64 import b64encode

from modules.requests.methods import Methods


def sendOK(request):
    request.send_response(200)
    request.send_header('Content-type', 'text/html')
    request.end_headers()


def home(method, request, url, parameters, data=None):
    """
    Home Page View
    """
    if method == Methods.GET:
        sendOK(request)
        request.wfile.write('HomePage'.encode())


def auth(method, request, url, parameters, data=None):

    credentials = ""
    with open('./credentials.json') as data:
        jsondata = json.load(data)
        credentials = f'{jsondata["username"]}:{jsondata["password"]}'
        credentials = b64encode(credentials.encode()).decode("ascii")

    def __authhead():
        request.send_response(401)
        request.send_header('WWW-Authenticate',
                            'Basic realm="Enter the admin credentials"')
        request.send_header('Content-type', 'text/html')
        request.end_headers()

    if request.headers['Authorization'] == None:
        __authhead()
        request.wfile.write('No credentials sent'.encode())

    elif request.headers['Authorization'] == f'Basic {credentials}':
        sendOK(request)
        request.wfile.write('authenticated!'.encode())
    else:
        __authhead()
        request.wfile.write('not authenticated'.encode())


def download(method, request, url, parameters, data=None):
    """
    Home Page View
    """
    if method == Methods.GET:
        request.send_response(200)
        request.send_header('Content-type', 'application/pdf')
        request.end_headers()

        with open('./files/cinematica.pdf', 'rb') as file:
            # Read the file and send the contents
            request.wfile.write(file.read())
