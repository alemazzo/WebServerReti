from modules.views import *

"""
Map each path to the relative view function
"""
urls_map = {
    '/': home,
    '/cinematica.pdf': download,
    '/auth': auth
}
