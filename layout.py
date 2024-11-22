from tabulate import tabulate


class Layout:
    def __init__(self):
        self._opcoes = []

    def basic(self):
        self._opcoes = [["Initial"]]
        print(tabulate(self._opcoes, showindex="always", tablefmt="rounded_grid"))

    def initial(self):
        self._opcoes = [["Initial"], ["Contacts"], ["New Contact"], ["Quit"]]

        print(tabulate(self._opcoes, showindex="always", tablefmt="rounded_grid"))

    def contact(self):
        self._opcoes = [["Initial"], ["New Contact"], ["Favorites"], ["Search"], [
            "Edit Contact"], ["Delete Contact"], ["Quit"]]

        print(tabulate(self._opcoes, showindex="always", tablefmt="rounded_grid"))
