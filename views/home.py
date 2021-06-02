from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/', methods=[Methods.GET])
def home(request: Request):
    """
    Home Page View
    """
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/index.html')
    response.send()
