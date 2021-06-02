from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/pubblica-esito', methods=[Methods.GET], auth=True)
def pubblica_esito(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/admin/pubblica_esito.html')
    response.send()


@app.route(route='/aggiungi-contatto', methods=[Methods.GET], auth=True)
def aggiungi_contatto(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/admin/aggiungi_contatto.html')
    response.send()
