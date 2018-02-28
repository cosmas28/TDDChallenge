import unittest

from phonebook import PhoneBook


class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = PhoneBook('Cosmas', '0729536851')

    def test_add_contact(self):
        self.assertTrue(self.phonebook.add_contact())


if __name__ == '__main__':
    unittest.main()
