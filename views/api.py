import json
import random

from modules.requests.methods import Methods
from modules.requests.request import Request
from modules.response.response import Response
from modules.app import app


@app.route(route='/api/orari', methods=[Methods.GET])
def orari(request: Request):
    """
    Get the orari of the hospital
    """
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/json')
    response.file('data/orari.json')
    response.send()


@app.route(route='/api/contatti', methods=[Methods.GET])
def get_contatti(request: Request):
    """
    Get all the contatti of the hospital
    """
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/json')
    response.file('data/contatti.json')
    response.send()


@app.route(route='/api/contatti/post', methods=[Methods.POST], auth=True)
def post_contatti(request: Request):
    """
    Post a new contatto.
    Authentication is required because only administrator
    can post or update a contatto.
    """
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/json')

    contatti = json.loads(open('data/contatti.json').read())
    contatti[request.data["nome"]] = request.data["numero"]

    # Write the output
    with open('data/contatti.json', 'w') as output:
        output.write(json.dumps(contatti))
    response.raw('{"status":"OK"}'.encode())

    response.send()


@app.route(route='/api/visite', methods=[Methods.GET], auth=True)
def get_visite(request: Request):
    """
    Get all the visite or a specific visita.
    Authentication is required because these are 
    sensitive data and only administrator can access
    this endpoint
    """
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/json')
    if not 'id' in request.parameters:
        # Get all the visite
        response.file('data/visite.json')
    else:
        # Get the visita with the specified ID
        _id = request.parameters['id']
        visite = json.loads(open('data/visite.json').read())
        visita = list(filter(lambda x: x['id'] == _id, visite))[0]
        response.raw(json.dumps(visita).encode())
    response.send()


@app.route(route='/api/visite/post', methods=[Methods.POST])
def post_visite(request: Request):
    """
    Post a new visita, no auth required because
    new visite are posted by simple client and not
    from the administrator
    """
    response = Response(request.connection)
    response.status_code(200)
    response.content_type('application/json')

    # Create the new visita
    visita = {
        'id': random.randint(0, 10000),
        'nome': request.data['nome'],
        'cognome': request.data['cognome']
    }

    # Load all visit and append the new visita
    visite = json.loads(open('data/visite.json').read())
    visite.append(visita)

    # Write the output
    with open('data/visite.json', 'w') as output:
        output.write(json.dumps(visite))

    # Return the new visita object
    response.raw(json.dumps(visita).encode())
    response.send()


@app.route(route='/api/esiti', methods=[Methods.GET])
def get_esiti(request: Request):
    """
    Get the esito with the specified ID if present, otherwise
    all the esiti will be returned
    """
    response = Response(request.connection)
    response.content_type('application/json')
    response.status_code(200)
    if not 'id' in request.parameters:
        # Get all the esiti
        response.file('data/esiti.json')
    else:
        # Get the esito with the specified ID
        try:
            _id = request.parameters['id']
            esiti = json.loads(open('data/esiti.json').read())
            esito = list(filter(lambda x: x['id'] == _id, esiti))[0]
            response.raw(json.dumps(esito).encode())
        except:
            response.status_code(404)
            response.raw(''.encode())
    response.send()


@app.route(route='/api/esiti/post', methods=[Methods.POST], auth=True)
def post_esiti(request: Request):
    """
    Post a new esito, auth is required because only the admin 
    can post an esito to this endpoint
    """
    response = Response(request.connection)
    response.content_type('application/json')
    response.status_code(200)

    # Add the new esito
    esito = request.data
    esiti = json.loads(open('data/esiti.json').read())
    esiti.append(esito)

    # Write the output
    with open('data/esiti.json', 'w') as output:
        output.write(json.dumps(esiti))
    response.raw('{"status":"OK"}'.encode())

    response.send()
