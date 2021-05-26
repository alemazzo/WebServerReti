def home(method, request, url, parameters, data=None):
    # Specifichiamo uno o più header
    request.send_header('Content-type', 'text/html')
    request.end_headers()

    request.wfile.write(bytes('helo', "utf8"))