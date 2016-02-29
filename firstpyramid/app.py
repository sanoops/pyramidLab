from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
	return Response("<h1> Hi Toobler</h1>")

if __name__ == '__main__':
    config = Configurator()
    config.add_view(hello_world)
    app = config.make_wsgi_app()
    print("http://127.0.0.1:8080/")
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
