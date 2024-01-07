import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from account import Account


class DatabaseHandler:
    def __init__(self, certificate_json_path):
        self.cred = credentials.Certificate(certificate_json_path)
        self.app = firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
    
    def user_collection(self):
        """Returns the collection reference to the users

        Returns:
            _type_: _description_
        """
        return self.db.collection("users")

    def get_all_users(self, converter_function):
        """Returns all the users

        Param:
            converter_function: This is a function reference that will be used to convert dict to to an account entity object
        Returns:
            _type_: _description_
        """

        docs = self.user_collection().stream()
        return [converter_function(x.to_dict()) for x in docs]

    def get_all_users_points(self, converter_function):
        query = self.user_collection().order_by("points", direction=firestore.Query.DESCENDING)
        docs = query.stream()
    
        return [converter_function(x.to_dict()) for x in docs]

if __name__ == "__main__":
    db_handler = DatabaseHandler()
    doc_ref = db_handler.user_collection().document("testing")
    doc_ref.set({"first": "Bach"})

    all_users = db_handler.get_all_users_points(Account.from_dict)

    if all_users:
        print("All Users:")
        for user in all_users:
            print("Username:", user.username)
            print("Time Spent:", user.time_spent)
            print("Points:", user.points)
            print("---")
    else:
        print("No users found.")