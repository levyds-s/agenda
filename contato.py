class Contact:
    def __init__(self, first_name, last_name, number, favorite):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._favorite = favorite
        self._id = number

    @property
    def name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def number(self):
        return self._number

    @property
    def id(self):
        return self._id

    @property
    def favorite(self):
        return self._favorite

    def __str__(self):
        if self._favorite == True:
            return f"★ {self._first_name} {self._last_name} | {self._number}"
        else:
            return f"{self._first_name} {self._last_name} | {self._number}"
