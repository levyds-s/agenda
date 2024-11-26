import sys
from contato import Contact


class Options:
    def __init__(self):
        self._list = []

    @property
    def size(self):
        return len(self._list)

    @property
    def contacts(self):
        return self._list

    def salvar_arquivo(self):
        with open("agenda.txt", "w") as arquivo:
            for contato in self._list:
                arquivo.write(
                    f"{contato._first_name}, {contato._last_name}, {contato.number}, {contato.favorite}\n")

    def ler_arquivo(self):
        with open("agenda.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for l in linhas:
                new_line = l.replace("\n", "")
                first_name, last_name, number, favorite = new_line.split(", ")
                if favorite == "True":
                    favorite = True
                else:
                    favorite = False
                item = Contact(first_name, last_name, number, favorite)
                self._list.append(item)

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
