import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        # This runs before every test
        self.account = BankAccount(123456, "Damion Ally")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 250.50)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 350.50)

    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 200.50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)  # more than available balance

    def test_sequence_of_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 400.50)

if __name__ == "__main__":
    unittest.main()