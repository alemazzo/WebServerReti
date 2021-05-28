from modules.requests.methods import Methods
from modules.response.response import Response
from modules.app import app


@app.route(route='/', methods=[Methods.GET])
def home(method, request, url, parameters, data=None):
    """
    Home Page View
    """
    response = Response(request)
    response.status_code(200)
    response.file('pages/index.html')
    response.send()


@app.route(route='/download.pdf', methods=[Methods.GET])
def download(method, request, url, parameters, data=None):
    """
    Home Page View
    """
    response = Response(request)
    response.status_code(200)
    response.content_type('application/pdf')
    response.file('files/download.pdf')
    response.send()


@app.route(route='/private', methods=[Methods.GET], auth=True)
def private(method, request, url, parameters, data=None):
    """
    Private Page View
    """
    response = Response(request)
    response.status_code(200)
    response.raw('Authenticated!'.encode())
    response.send()
