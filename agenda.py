import sys


class Options:
    def __init__(self):
        self._list = []

    @property
    def size(self):
        return len(self._list)

    @property
    def contacts(self):
        return self._list

    def favorites(self):
        pass

    def add_number(self, contact):
        self._list.append(contact)

    def delete_contacts(self, contact):
        new_list = []
        for item in self._list:
            if item.id != contact.id:
                new_list.append(item)
        self._list = new_list

    def edit(self, new_contact):
        for item in self._list:
            if new_contact.id == item.id:
                pass

    def search(self, contact):
        for item in self._list:
            if contact._first_name == item._first_name:
                return item
    # ☆⛤★
