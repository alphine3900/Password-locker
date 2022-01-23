from passwords import Password
import unittest


class TestPasswords(unittest.TestCase):
    def tearDown(self):
        '''
        this test clears the user_passwords array beore every test
        '''
        Password.user_passwords = []

    def setUp(self):
        '''
        this test creates a new instance of the passwords class
        before every test
        '''
        self.new_password = Password('facebook', '12345')

    def test_init(self):
        '''
        this test checks whether the data enterd into the properties if called wll appear
        '''
        self.assertEqual(self.new_password.page, 'facebook')
        self.assertEqual(self.new_password.password, '12345')