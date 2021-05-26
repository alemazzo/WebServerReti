
import sys
import signal
import http.server
import socketserver
import json
from modules.methods import *
from modules.urls import urls_map

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888


class Handler(http.server.BaseHTTPRequestHandler):

    def send_request_to_view(self, method, data=None):
        """
        Handle the generic request and send it to the correct view
        """

        # Unpack the url
        url, parameters = self.unpack_path(self.path)

        # Log the request
        print(method + " url = " + url + " parameters = " + str(parameters) + " data = " + str(data))

        # Check if the urls is valid, otherwise send a 404
        if url in urls_map:
            view = urls_map[url]
            view(method, self, url, parameters, data)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('404 - Not Found', "utf8"))


    def unpack_path(self, path):
        """
        Unpack the request and split the url from the parameters
        """
        url = self.path
        parameters = {}
        if '?' in url:
            url, params = self.path.split('?')
            params = params.split('&')
            for param in params:
                name, value = param.split('=')
                parameters.update({name: value})
        return url, parameters

    def do_GET(self):
        """
        Handle the GET requests
        """
        self.send_request_to_view(Methods.GET)

    
    def do_POST(self):
        """
        Handle the POST requests
        TODO: add a try to check if data is json loadable or not
        """
        content_len = int(self.headers['content-length'])
        data = json.loads(self.rfile.read(content_len).decode())
        self.send_request_to_view(Methods.POST, data)



# Nota ForkingTCPServer non funziona su Windows come os.fork ()
# La funzione non è disponibile su quel sistema operativo. Invece dobbiamo usare il
# ThreadingTCPServer per gestire più richieste
server = socketserver.ThreadingTCPServer(
    ('', port), Handler)

# Assicura che da tastiera usando la combinazione
# di tasti Ctrl-C termini in modo pulito tutti i thread generati
server.daemon_threads = True
# il Server acconsente al riutilizzo del socket anche se ancora non è stato
# rilasciato quello precedente, andandolo a sovrascrivere
server.allow_reuse_address = True

# definiamo una funzione per permetterci di uscire dal processo tramite Ctrl-C
def signal_handler(signal, frame):
    print('Exiting http server (Ctrl+C pressed)')
    try:
        if(server):
            server.server_close()
    finally:
        sys.exit(0)


# interrompe l’esecuzione se da tastiera arriva la sequenza (CTRL + C)
signal.signal(signal.SIGINT, signal_handler)

# entra nel loop infinito
try:
    while True:
        # sys.stdout.flush()
        server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
