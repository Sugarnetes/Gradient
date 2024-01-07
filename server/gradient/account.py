
from firebase_admin import firestore

class Account:
    def __init__(self, username, time_spent=0, points=0):
        self.username = username
        self.time_spent = time_spent
        self.points = time_spent

    def to_dict(self):
        return {
            "username": self.username,
            "time_spent": self.time_spent,
            "points": self.points,
        }
    
    @staticmethod
    def from_dict(source):
        username = source.get("username")
        time_spent = source.get("time_spent", 0)
        points = source.get("points", 0)
        return Account(username, time_spent, points)

    def add_time(self, time_spent: int):
        self.time_spent += time_spent
    
    def save_to_db(self, db):
        doc_ref = db.collection("users").document(self.username)
        doc_ref.set(self.to_dict())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.username == other.username
        else:
            return False

    @staticmethod
    def retrieve_from_db_ordered_by_points(db):
        query = db.collection("users").order_by("points", direction=firestore.Query.DESCENDING)
        docs = query.stream()

        accounts = []
        for doc in docs:
            account_data = doc.to_dict()
            account = Account.from_dict(account_data)
            accounts.append(account)

        return accounts