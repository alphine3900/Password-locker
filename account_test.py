from account import Acc
import unittest

class TestAccount(unittest.TestCase):
    def tearDown(self):
        Accounts.user_accounts = []

    def setUp(self):
        '''
        this test runs before every test occurs
        '''
        self.new_account = Accounts('hamida', 'mstafa', 'mids', '1996')

    def test_init(self):
        '''
        a test to assert whether the values entered would appear when the roperty is called
        '''
        self.assertEqual(self.new_account.first_name, 'hamida')
        self.assertEqual(self.new_account.last_name, 'mstafa')
        self.assertEqual(self.new_account.user_name, 'mids')
        self.assertEqual(self.new_account.password, '1996')
+9
def test_save_account(self):
        '''
        a test to check whether the save function works
        '''
        self.new_account.save_account()
        self.assertEqual(len(Accounts.user_accounts), 1)

def test_save_multiple_accounts(self):