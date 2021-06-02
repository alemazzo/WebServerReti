from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/orari-ospedale', methods=[Methods.GET])
def orari_ospedale(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/services/orari_ospedale.html')
    response.send()


@app.route(route='/prenota-una-visita', methods=[Methods.GET])
def prenota_una_visita(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/services/prenota_una_visita.html')
    response.send()


@app.route(route='/risultati-esami', methods=[Methods.GET])
def risulati_esami(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/services/risultati_esami.html')
    response.send()


@app.route(route='/info', methods=[Methods.GET])
def info(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/services/info.html')
    response.send()
