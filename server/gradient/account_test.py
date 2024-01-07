import unittest
from account import Account


class MyTestCase(unittest.TestCase):

    def test_account_construction(self):
        expected = Account("testing1")
        test_input = {"username": "testing1", "time_spent": 0, "points": 0}
        self.assertEqual(expected, Account.from_dict(test_input))
    
    def test_from_dict(self):
        expected = Account("testing1", 0, 0)
        test_input = {"username": "testing1", "time_spent": 0, "points": 0}
        self.assertEqual(expected, Account.from_dict(test_input))
        

if __name__ == '__main__':
    unittest.main()
