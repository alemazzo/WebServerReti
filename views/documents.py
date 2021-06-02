from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/normativa.pdf', methods=[Methods.GET])
def normativa(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/pdf')
    response.file('files/normativa.pdf')
    response.send()


@app.route(route='/regolamento.pdf', methods=[Methods.GET])
def regolamento(request: Request):
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/pdf')
    response.file('files/regolamento.pdf')
    response.send()
