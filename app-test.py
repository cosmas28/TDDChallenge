import unittest

from phonebook import PhoneBook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook('Cosmas', '0729536851')

    def test_add_contact(self):
        self.assertEqual(self.phonebook.add_contact(), '0729536851')

    def test_delete_contact(self):
        self.phonebook.add_contact()
        self.assertTrue(self.phonebook.delete_contact('Cosmas'))


if __name__ == '__main__':
    unittest.main()
