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
        '''
        a test that checks whether both values appended to the array are actually present and returns the acount itself
        '''
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.assertEqual(len(Accounts.user_accounts), 2)

def test_del_account(self):
        '''
        test that check the delete function
        '''
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        self.new_account.delete_account()
        self.assertEqual(len(Accounts.user_accounts), 1)

def test_find_account_by_username(self):
        '''
        test to check whether the function used to find accounts really works
        '''
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        found_account = Accounts.find_by_user_name('ijkl')
        self.assertEqual(found_account.user_name, test_account.user_name)
        def test_account_exists(self):
        '''
        unlike the previous test this test returns a true/false soort of answer depending on whether the account exists or not
        '''
        self.new_account.save_account()
        test_account = Accounts('abcd', 'efgh', 'ijkl', 'mnop')
        test_account.save_account()
        account_exists = Accounts.account_exists('ijkl')
        self.assertTrue(account_exists)

def test_display_accounts(self):
        '''
        a test to check the display accounts function
        '''
        self.assertEqual(Accounts.display_accounts(),
                         Accounts.user_accounts)


if __name__ == '__main__':
    unittest.main()