import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
from summarizer import Summarize

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    clients = set()
    initial_load_completed = False

    def check_origin(self, origin):
        return True

    def open(self):
        print("WebSocket opened")
        WebSocketHandler.clients.add(self)

        if not WebSocketHandler.initial_load_completed:
            generated_file_path = r"C:\umer files\Programming PREJE'S\Gradient\server\summarized_content.pdf"
            if os.path.exists(generated_file_path):
                with open(generated_file_path, 'rb') as file:
                    file_data = file.read()
                    self.write_message(file_data, binary=True)
            else:
                self.write_message("Generated file not found")

    def on_message(self, message):
        if message == "request_summary_file" and self.application.uploaded_file_path:
            generated_file_path = r"C:\umer files\Programming PREJE'S\Gradient\server\summarized_content.pdf"
            if os.path.exists(generated_file_path):
                with open(generated_file_path, 'rb') as file:
                    file_data = file.read()
                    self.write_message(file_data, binary=True)
            else:
                self.write_message("Generated file not found")
        elif message == "delete_file_request":
            self.delete_generated_file()

        elif message == "initial_load_completed":
            WebSocketHandler.initial_load_completed = True

    def delete_generated_file(self):
        if self.application.uploaded_file_path:
            os.remove(self.application.uploaded_file_path)
            self.application.uploaded_file_path = None
            print("File deleted successfully")
        else:
            print("File not found or already deleted")

    def on_close(self):
        print("WebSocket closed")
        WebSocketHandler.clients.remove(self)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")

class UploadHandler(tornado.web.RequestHandler):
    async def send_file_through_websocket(self, file_path):
        ws_clients = WebSocketHandler.clients
        if ws_clients:
            for client in ws_clients:
                file_data = None
                if os.path.exists(file_path):
                    with open(file_path, 'rb') as file:
                        file_data = file.read()
                if file_data:
                    await client.write_message(file_data, binary=True)
                else:
                    await client.write_message("Generated file not found")

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3003")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST")

    async def post(self):
        uploaded_file = self.request.files.get('pdfFile')
        if uploaded_file:
            file_data = uploaded_file[0]['body']
            file_name = uploaded_file[0]['filename']

            current_directory = os.path.dirname(os.path.abspath(__file__))
            upload_path = os.path.join(current_directory, 'uploads')

            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            sanitized_file_name = ''.join(c for c in file_name if c.isalnum() or c in ['.', '_', '-'])
            output_file_path = os.path.join(upload_path, sanitized_file_name)
            print("Saving file to:", output_file_path)

            self.application.uploaded_file_path = output_file_path

            with open(output_file_path, 'wb') as output_file:
                output_file.write(file_data)

            ans = Summarize(output_file_path)
            ans.execute_summary()

            await self.send_file_through_websocket(r"C:\umer files\Programming PREJE'S\Gradient\server\summarized_content.pdf")

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
    app.listen(8000)
    print("Server started.")
    tornado.ioloop.IOLoop.current().start()