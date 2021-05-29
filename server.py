import sys
import os

from modules.app import app


"""
Select the port
"""
if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8888

"""
Very important!!
Load all modules in views folder in order to execute all the
app.routes decorator which add the mapping of the url
to the function to execute
"""
for entry in os.scandir('views'):
    if entry.is_file() and entry.name[-3:].lower() == '.py':
        string = f'from views import {entry.name}'[:-3]
        exec(string)

# Start the application
app.start(port)
