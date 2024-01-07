import unittest
from server.my_db_handler.my_db_handler import DatabaseHandler

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.db_object = DatabaseHandler(
            "../firebase_credentials/hacked24-60c88-firebase-adminsdk-5fu9m-0ba7ceb240.json")
    def test_db_transaction(self):
        store = {"first": "Bach", "middle": "none"}
        test_ref = self.db_object.user_collection().document("unit_test_1")
        test_ref.set(store)

        self.assertEqual(test_ref.get().to_dict(), store)

        test_ref.delete()

if __name__ == '__main__':
    unittest.main()
