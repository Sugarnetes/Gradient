import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import random
import string
from pdfreader import PdfReader

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/websocket", WebSocketHandler),
        ]
        tornado.web.Application.__init__(self, handlers)

'''
 Websocket handler for communicating between client timer and server
'''
class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        print("Received message:", message)
        # Here you can handle the message
        # For example, parse JSON and process data

    def on_close(self):
        print("WebSocket closed")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files.get('file', []) # allows a file with any name to be uploaded
        for file_data in files:
            original_fname = file_data['filename']
            upload_path = "uploads/"

            # Check if the directory exists, create it if not
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            output_file_path = os.path.join(upload_path, original_fname)
            print("Saving file to:", output_file_path)  # Add a debug statement

            output_file = open(output_file_path, 'wb')
            output_file.write(file_data['body'])
            output_file.close()

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),  # Add a handler for the root URL
        (r"/upload", UploadHandler),
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started.")
    tornado.ioloop.IOLoop.current().start()
