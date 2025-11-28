import unittest
from Account_Class import Account, Saving_Accounts

class TestBankSystem(unittest.TestCase):

    # This runs BEFORE every single test method
    # It sets up a fresh account so tests don't interfere with each other
    def setUp(self):
        self.user = Account("Test User", 1234, 1000)
        self.saver = Saving_Accounts("Saver User", 9999, 1000)

    # --- STANDARD ACCOUNT TESTS ---

    def test_deposit(self):
        self.user.deposit(500)
        # Assert: We expect balance to be 1500
        self.assertEqual(self.user.check_balance(), 1500)

    def test_withdraw(self):
        self.user.withdraw(200)
        self.assertEqual(self.user.check_balance(), 800)

    def test_insufficient_funds(self):
        # Try to withdraw 2000 (Account only has 1000)
        self.user.withdraw(2000)
        # Balance should NOT change
        self.assertEqual(self.user.check_balance(), 1000)

    def test_negative_deposit(self):
        self.user.deposit(-500)
        self.assertEqual(self.user.check_balance(), 1000)

    # --- SAVINGS ACCOUNT TESTS ---

    def test_savings_interest(self):
        # Savings Account adds 5% interest
        # Deposit 100 -> Interest is 5 -> Total added 105
        self.saver.deposit(100)
        self.assertEqual(self.saver.check_balance(), 1105)

    def test_transaction_history(self):
        self.user.deposit(100)
        self.user.withdraw(50)
        history = self.user.get_history()
        
        # We expect 2 records in the list
        self.assertEqual(len(history), 2)
        # Verify the message content
        self.assertIn("Deposited: $100", history[0])
        self.assertIn("Withdrew: $50", history[1])

if __name__ == '__main__':
    unittest.main()