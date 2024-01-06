import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class DatabaseHandler:
    def __init__(self):
        self.cred = credentials.Certificate("../../firebase_credentials/hacked24-60c88-firebase-adminsdk-5fu9m-0ba7ceb240.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
    
    def user_collection(self):
        return self.db.collection("users")


if __name__ == "__main__":
    db_handler = DatabaseHandler()
    doc_ref = db_handler.user_collection().document("testing")
    doc_ref.set({"first": "Bach"})