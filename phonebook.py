"""phonebook app that allows users to add, update, delete and view contacts"""


class PhoneBook:
    def __init__(self, name, phone_number):
        self._name = name
        self.p_number = phone_number
        self.contact_list = []

    def add_contact(self):
        _contact = {
            'name': self._name,
            'phone': self.p_number
        }
        self.contact_list.append(_contact)
        if _contact not in self.contact_list:
            return False

        return True
