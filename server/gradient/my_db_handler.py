import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from account import Account


class DatabaseHandler:
    def __init__(self):
        """The firebase app must be initialized in main for this constructor to work
        """
        self.db = firestore.client()
    
    def user_collection(self):
        """Returns the collection reference to the users

        Returns:
            _type_: _description_
        """
        return self.db.collection("users")
    
    def get_user_hash(self, name: str):
        """This method gets the dictionary of a username from the database

        Args:
            name (str): The username that is being searched for.

        Returns:
            dict: The dict representing the document
        """

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

    def get_all_users_points(self):
        query = self.user_collection().order_by("points", direction=firestore.Query.DESCENDING)
        docs = query.stream()
        return [Account.from_dict(x.to_dict()) for x in docs]
    
