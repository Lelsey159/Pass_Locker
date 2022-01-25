from password import Password
import unittest


class TestPasswords(unittest.TestCase):
    def tearDown(self):
       
        Password.user_passwords = []

    def setUp(self):
        
        self.new_password = Password('facebook', '@2020')

    def test_init(self):
        
        self.assertEqual(self.new_password.page, 'facebook')
        self.assertEqual(self.new_password.password, '@2020')

    def test_save_page(self):
       
        self.new_password.save_page()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_save_multiple(self):
        
        self.new_password.save_page()
        test_pass = Password('instagram', '@2021')
        test_pass.save_page()
        self.assertEqual(len(Password.user_passwords), 2)

    def test_delete_page(self):
        
        self.new_password.save_page()
        test_pass = Password('instagram', '@2021')
        test_pass.save_page()
        self.new_password.delete_page()
        self.assertEqual(len(Password.user_passwords), 1)

    def test_display_page(self):
        self.assertEqual(Password.display_page(), Password.user_passwords)

    def test_find_page(self):
       
        self.new_password.save_page()
        test_pass = Password('instagram', '@2021')  # new contact
        test_pass.save_page()
        found_page = Password.find_by_page('instagram')
        self.assertEqual(found_page.page, test_pass.page)

    def page_exists(self):
        
        self.new_password.save_page()
        test_pass = Password('instagram', '@2021')  # new contact
        test_pass.save_page()
        page_exist = Password.page_exists('instagram')
        self.assertTrue(page_exist)


if __name__ == '__main__':
    unittest.main()