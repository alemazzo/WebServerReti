from modules.requests.methods import Methods
from modules.response.response import Response
from modules.app import app


@app.route(route='/index', methods=[Methods.GET])
def home(method, request, url, parameters, data=None):
    """
    Home Page View
    """
    response = Response(request)
    response.status_code(200)
    response.file('pages/index.html')
    response.send()
