mport sae
from mylibrary import wsgi

application = sae.create_wsgi_app(wsgi.application)

