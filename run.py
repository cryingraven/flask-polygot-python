from app import app
import controller
from gevent.pywsgi import WSGIServer
http_server = WSGIServer(('', 8012), app)
http_server.serve_forever()

