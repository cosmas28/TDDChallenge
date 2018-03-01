"""phonebook app that allows users to add, update, delete and view contacts"""


class PhoneBook:
    def __init__(self, name, phone_number):
        self._name = name
        self.p_number = phone_number
        self.contact_list = {}

    def add_contact(self):
        self.contact_list[self._name] = self.p_number
        if self.contact_list.get(self._name) is None:
            return False

        return True

    def delete_contact(self, name):
        if self.contact_list[name]:
            del self.contact_list[name]
        else:
            raise KeyError

        if name in self.contact_list:
            return False
        return True
