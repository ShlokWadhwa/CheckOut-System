# Shlok Wadhwa, Project, CIS345 T/Th 10:30-11:45


class Customer:
    """Customer class defines common information for all students
    Creating appropriate getters and setters as well"""

    def __init__(self, acc_num=int(), fname=str(), lname=str(), pin=0000, balance=int(), isemployee=False):
        self.accnum = acc_num
        self.fname = fname
        self.lname = lname
        self.pin = pin
        self.balance = balance
        self.isemployee = isemployee


    @property
    def fname(self):
        return self.__fname.capitalize()

    @fname.setter
    def fname(self, newfname):
        if newfname.isalpha():
            self.__fname = newfname
        else:
            self.__fname = 'Unknown'

    @property
    def lname(self):
        return self.__lname.capitalize()

    @lname.setter
    def lname(self, newlname):
        if newlname.isalpha():
            self.__lname = newlname
        else:
            self.__lname = 'Uknown'

    @property
    def accnum(self):
        return f'{self.__accnum:}'

    @accnum.setter
    def accnum(self, new_acc):
        if new_acc.isnumeric():
            self.__accnum = new_acc
        else:
            self.__accnum = 'Unknown'

    @property
    def pin(self):
        return f'{self.__pin:<4}'

    @pin.setter
    def pin(self, new_pin):
        if new_pin.isnumeric() and len(new_pin) == 4:
            self.__pin = new_pin
        else:
            self.__pin = 'Unknown'

    @property
    def balance(self):
        return f'{self.__balance}'

    @balance.setter
    def balance(self, new_balance):
        if new_balance != 0:
            self.__balance = new_balance

    @property
    def isemployee(self):
        return self.__isemployee

    @isemployee.setter
    def isemployee(self, arg):
        self.__isemployee = arg

    def __str__(self):
        """Overrides the string representation of a Customer"""
        return f'{self.fname} {self.lname}'

