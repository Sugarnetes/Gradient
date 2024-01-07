import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path
import random
import string
from pdfreader import PdfReader

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")

class UploadHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # Set headers to allow requests from your React frontend
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3003")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST")
        
    def post(self):
        uploaded_file = self.request.files.get('pdfFile')
        if uploaded_file:
            file_data = uploaded_file[0]['body']
            file_name = uploaded_file[0]['filename']

            current_directory = os.path.dirname(os.path.abspath(__file__))
            upload_path = os.path.join(current_directory, 'uploads')
            output_file_path = os.path.join(upload_path, file_name)
            print("Saving file to:", output_file_path)  # Add a debug statement

            output_file = open(output_file_path, 'wb')
            output_file.write(file_data)
            output_file.close()
            
            self.write('File uploaded successfully!')
        else:
            self.set_status(400)
            self.write('No file uploaded.')


def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),  # Add a handler for the root URL
        (r"/upload", UploadHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server started.")
    tornado.ioloop.IOLoop.current().start()