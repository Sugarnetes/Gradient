import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
from firebase_admin import credentials
import firebase_admin
import os.path
from summarizer import Summarize
from pdfreader import PdfReader
import sys
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if mod_path not in sys.path:
    sys.path.insert(1, mod_path)
del mod_path
from gradient.account import Account
from gradient.my_db_handler import DatabaseHandler

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload", UploadHandler),
            (r"/websocket", WebSocketHandler),
        ]
        tornado.web.Application.__init__(self, handlers)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        # This one is expensive
        db_handler = DatabaseHandler()
        name, time_spent_string = message[1:-1].split(',')
        time_spent = float(time_spent_string)
        db_hash = db_handler.get_user_hash(name)
        target_account = Account.from_dict(db_hash)
        target_account.add_time(time_spent)

        target_account.save_to_db(db_handler.get_db())
        
        print(name)
        print(time_spent)
        

    def on_close(self):
        print("WebSocket closed")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")

class UploadHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
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

            # Ensure the directory exists or create it
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            # Sanitize the filename
            sanitized_file_name = ''.join(c for c in file_name if c.isalnum() or c in ['.', '_', '-'])
            output_file_path = os.path.join(upload_path, sanitized_file_name)
            print("Saving file to:", output_file_path)
            output_file = open(output_file_path, 'wb')
            output_file.write(file_data)
            output_file.close()

            ans = Summarize(output_file_path)
            ans.execute_summary()
            self.write('File uploaded successfully!')
        else:
            self.set_status(400)
            self.write('No file uploaded.')

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r"/upload", UploadHandler),
        (r"/websocket", WebSocketHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    cred = credentials.Certificate(
        "server/firebase_credentials/hacked24-60c88-firebase-adminsdk-5fu9m-0ba7ceb240.json")
    app = firebase_admin.initialize_app(cred)
    print("Server started.")
    tornado.ioloop.IOLoop.current().start()
