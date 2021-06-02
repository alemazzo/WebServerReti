from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/cambia-orari', methods=[Methods.GET], auth=True)
def cambia_orari(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/admin/cambia_orari.html')
    response.send()


@app.route(route='/elenco-dipendenti', methods=[Methods.GET], auth=True)
def elenco_dipendenti(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/admin/elenco_dipendenti.html')
    response.send()


@app.route(route='/dashboard', methods=[Methods.GET], auth=True)
def dashboard(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.file('pages/admin/dashboard.html')
    response.send()
