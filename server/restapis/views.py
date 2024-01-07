from tornado.web import RequestHandler
import os

class IndexHandler(RequestHandler):
    def get(self):
        self.render("tornadoUpload.html")


class UploadHandler(RequestHandler):
    def post(self):
        files = self.request.files.get('file', [])  # allows a file with any name to be uploaded
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
