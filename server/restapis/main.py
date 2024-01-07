from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.log import enable_pretty_logging
from views import IndexHandler, UploadHandler


def make_app():
    return Application([
        (r"/", IndexHandler),  # Add a handler for the root URL
        (r"/upload", UploadHandler),
    ])


def main(port_number: int):
    enable_pretty_logging()
    app = make_app()
    http_server = HTTPServer(app)
    http_server.listen(port_number)
    print(f"Listening on port {port_number}")
    IOLoop.current().start()
    

if __name__ == "__main__":
    print(f"Webserver starting")
    main(8888)
    print(f"Webserver ending")
