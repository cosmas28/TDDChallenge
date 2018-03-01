"""phonebook app that allows users to add, update, delete and view contacts"""


class PhoneBook:
    def __init__(self, name, phone_number):
        self._name = name
        self.p_number = phone_number
        self.contact_list = {}

    def add_contact(self):
        self.contact_list[self._name] = self.p_number

        if self._name not in self.contact_list:
            return "Contact not added. Please try again!!"

        return self.contact_list[self._name]

    def view_contact(self):
        view_list = []
        if len(self.contact_list) == 0:
            return "The phone book is empty!"
        else:
            for key, value in self.contact_list.items():
                view_list.append((key, value))

        return view_list

