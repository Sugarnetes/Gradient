import unittest
import firebase_admin
from firebase_admin import credentials
from my_db_handler import DatabaseHandler

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_object = DatabaseHandler()

    def test_db_transaction(self):
        store = {"first": "Bach", "middle": "none"}
        test_ref = self.db_object.user_collection().document("unit_test_1")
        test_ref.set(store)

        self.assertEqual(test_ref.get().to_dict(), store)

        test_ref.delete()
    
    def test_get_user_hash(self):
        expected_1 = {"username": "Test1", "time_spent": 0, "points": 0}
        self.assertEqual(expected_1, self.db_object.get_user_hash("Test1"))
        self.db_object.user_collection().document("Test1").delete()

if __name__ == '__main__':
    cred = credentials.Certificate(
    "firebase_credentials/hacked24-60c88-firebase-adminsdk-5fu9m-0ba7ceb240.json")
    app = firebase_admin.initialize_app(cred)
    unittest.main()
