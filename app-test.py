import unittest

from phonebook import PhoneBook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook('Cosmas', '0729536851')

    def test_add_contact(self):
        self.assertEqual(self.phonebook.add_contact(), '0729536851')

    def test_update_contact(self):
        self.phonebook.add_contact()
        result = self.phonebook.update_contact('Cosmas', '1234')
        self.assertEqual(result, '1234')


if __name__ == '__main__':
    unittest.main()
