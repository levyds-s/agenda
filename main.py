from agenda import Options
from contato import Contact
from layout import Layout
import os
import sys


class Main:
    INICIAL = 0
    LISTAR = 1
    ADICIONAR = 2
    EDITAR = 3
    REMOVER = 4
    PESQUISAR = 5
    FAVORITOS = 6

    def __init__(self):
        self.estado = Main.INICIAL
        self.agenda = Options()
        self.layout = Layout()

    def iniciar(self):
        print()
        self.layout.initial()
        opcao = int(input("Enter a Number: "))
        if opcao == 0:
            pass
        elif opcao == 1:
            self.estado = Main.LISTAR
        elif opcao == 2:
            self.estado = Main.ADICIONAR
        elif opcao == 3:
            sys.exit()

    def adicionar(self):
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        phone = input("Phone: ").strip()
        favorite = input("Number is favorite? (Y/N): ").strip().lower()

        if favorite == "y" or favorite == "yes":
            favorite = True
        else:
            favorite = False
        new_item = Contact(first_name, last_name, phone, favorite)
        self.agenda.add_number(new_item)
        self.estado = Main.INICIAL

    def listar(self):
        if self.agenda.size == 0:
            print("Empty")
        else:
            for contact in self.agenda.contacts:
                print(contact)
        print()
        self.layout.contact()
        opcao = int(input("Enter a Number: "))
        if opcao == 0:
            self.estado = Main.INICIAL
        elif opcao == 1:
            self.estado = Main.ADICIONAR
        elif opcao == 2:
            self.estado = Main.FAVORITOS
        elif opcao == 3:
            self.estado = Main.PESQUISAR
        elif opcao == 4:
            self.estado = Main.EDITAR
        elif opcao == 5:
            self.estado = Main.REMOVER
        elif opcao == 6:
            sys.exit()

    def editar(self):
        number = input("which contact to edit? number: ").strip()
        for contato in self.agenda.contacts:
            if number == contato.id:
                print(contato)
                this_is = input("Is this the contact? (Y/N): ").strip().lower()
                if this_is == "y" or this_is == "yes":
                    self.agenda.delete_contacts(contato)
                    new_first_name = input("New first name: ")
                    new_last_name = input("New last name: ")
                    new_phone = input("New phone: ")
                    favorite = input(
                        "Number is favorite? (Y/N): ").strip().lower()

                    if favorite == "y" or favorite == "yes":
                        favorite = True
                    else:
                        favorite = False
                    contact_update = Contact(
                        new_first_name, new_last_name, new_phone, favorite)
                    self.agenda.add_number(contact_update)
                    self.estado = Main.INICIAL

    def favoritos(self):
        for contato in self.agenda.contacts:
            if contato._favorite == True:
                print(contato)
        print()
        self.layout.initial()
        opcao = int(input("Enter a Number: "))
        if opcao == 0:
            self.estado = Main.INICIAL
        elif opcao == 1:
            self.estado = Main.LISTAR
        elif opcao == 2:
            self.estado = Main.ADICIONAR
        elif opcao == 3:
            sys.exit()

    def remover(self):
        number = input("Which contact to remove? Number: ").strip()
        for it in self.agenda.contacts:
            if it.id == number:
                self.agenda.delete_contacts(it)
                self.estado = Main.INICIAL

    def pesquisar(self):
        name = input("What's the name? (First Name) :").strip()
        for item in self.agenda.contacts:
            if item._first_name == name:
                print(item)

        self.layout.basic()
        opcao = int(input("Enter a Number: "))
        if opcao == 0:
            self.estado = Main.INICIAL

    def rodar(self):
        # opcoes = {Main.INICIAL: self.iniciar(), Main.LISTAR: self.listar(), Main.ADICIONAR: self.adicionar(),
       #           Main.EDITAR: self.editar(), Main.REMOVER: self.remover(), Main.PESQUISAR: self.pesquisar(), Main.FAVORITOS: self.favoritos()}

        while True:
            # opcoes[self.estado]
            os.system("clear")

            if self.estado == Main.INICIAL:
                self.iniciar()
            elif self.estado == Main.LISTAR:
                self.listar()
            elif self.estado == Main.ADICIONAR:
                self.adicionar()
            elif self.estado == Main.EDITAR:
                self.editar()
            elif self.estado == Main.REMOVER:
                self.remover()
            elif self.estado == Main.PESQUISAR:
                self.pesquisar()
            elif self.estado == Main.FAVORITOS:
                self.favoritos()


comecar = Main()
comecar.rodar()
