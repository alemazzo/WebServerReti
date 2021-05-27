
import sys
import signal
import http.server
import socketserver
import json
from modules.handler import Handler

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

server = socketserver.ThreadingTCPServer(('', port), Handler)
server.daemon_threads = True
server.allow_reuse_address = True


def signal_handler(signal, frame):
    print('Exiting http server (Ctrl+C pressed)')
    try:
        if(server):
            server.server_close()
    finally:
        sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        # sys.stdout.flush()
        server.serve_forever()
except KeyboardInterrupt:
    pass

server.server_close()
