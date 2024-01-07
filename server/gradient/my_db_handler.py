import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class DatabaseHandler:
    def __init__(self):
        """For high speed prototyping, we need the firebase app to be initialized in main
        """
        self.db = firestore.client()
    
    def user_collection(self):
        """Returns the collection reference to the users

        Returns:
            _type_: _description_
        """
        return self.db.collection("users")
    
    def get_user_hash(self, name: str):

        cache = self.user_collection().document(name).get().to_dict()
        if not cache:
            new_account = {"username": name, "time_spent": 0, "points": 0}
            self.user_collection().document(name).set(new_account)
            cache = new_account
        return cache


    def get_all_users(self, converter_function):
        """Returns all the users

        Param:
            converter_function: This is a function reference that will be used to convert dict to to an account entity object
        Returns:
            _type_: _description_
        """

        docs = self.user_collection().stream()
        return [converter_function(x.to_dict()) for x in docs]
    
    def get_db(self):
        return self.db


if __name__ == "__main__":
    db_handler = DatabaseHandler()
    doc_ref = db_handler.user_collection().document("testing")
    doc_ref.set({"first": "Bach"})