import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from account import Account
from account import Account


class DatabaseHandler:
    def __init__(self):
        self.cred = credentials.Certificate("firebase_credentials/hacked24-60c88-firebase-adminsdk-5fu9m-0ba7ceb240.json")
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
    
    def user_collection(self):
        """Returns the collection reference to the users

        Returns:
            _type_: _description_
        """
        return self.db.collection("users")

    def get_all_users(self):
        """Returns all the users

        Param:
            converter_function: This is a function reference that will be used to convert dict to to an account entity object
        Returns:
            _type_: _description_
        """
        docs = self.user_collection().stream()
        return [Account.from_dict(x.to_dict()) for x in docs]
       

    def save_to_db(self, db):
        doc_ref = db.collection("users").document(self.username)
        doc_ref.set(self.to_dict())
    def save_to_db(self, db):
        doc_ref = db.collection("users").document(self.username)
        doc_ref.set(self.to_dict())

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    doc_ref = db_handler.user_collection().document("testing")
    doc_ref.set({"first": "Bach"})
    all_users = db_handler.get_all_users()
    for user in all_users:
        print(f"Username: {user.username}")