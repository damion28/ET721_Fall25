import unittest
from bankaccount import BankAccount

print("\n---- exercise: Unit testing the BankAccount class ----")


class TestBankAccount(unittest.TestCase):

    # Example 1.1: setup for all tests
    def setUp(self):
        self.account = BankAccount("Damion Ally", 250.50)

    # Example 1.2: test that account initializes correctly
    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 250.50)

    # Example 1.3: test deposit
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 350.50)

    # Example 1.4: test withdraw
    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 200.50)

    # Example 1.5: test insufficient funds (should raise ValueError)
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1000)

    # Example 1.6: test negative deposit (should raise ValueError)
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    # Example 1.7: test sequence of transactions
    def test_sequence_of_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 400.50)


if __name__ == "__main__":
    unittest.main()
