class Student:
    def __init__(self, full_name, group_number, birth_date=None, address=None):
        self.__full_name = full_name
        self.__group_number = group_number
        self.__birth_date = birth_date
        self.__address = address

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_group_number(self):
        return self.__group_number

    def set_group_number(self, group_number):
        self.__group_number = group_number

    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address