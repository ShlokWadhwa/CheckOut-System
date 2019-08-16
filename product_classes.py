# Shlok Wadhwa, Project, CIS345 T/Th 10:30-11:45


class Product:
    """Product class defines information for the parent products
    Creating getters and setters for all attributes"""

    def __init__(self, prodid=str(), desc=str(), quantity=int(), price=int()):
        self.prodid = prodid
        self.desc = desc
        self.quantity = quantity
        self.price = price

    @property
    def prodid(self):
        return f'{self.__prodid}'

    @prodid.setter
    def prodid(self, new_prodid):
        if new_prodid != '':
            self.__prodid = new_prodid
        else:
            self.__prodid = 'Unknown'

    @property
    def desc(self):
        return f'{self.__desc}'

    @desc.setter
    def desc(self, new_desc):
        if new_desc != '':
            self.__desc = new_desc
        else:
            self.__desc = 'Unknown'

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quan):
        if new_quan != 0:
            self.__quantity = new_quan
        else:
            self.__quantity = 'Unknown'

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price != 0:
            self.__price = new_price
        else:
            self.__price = 'Unknown'

    def __str__(self):
        """Overrides the string representation of a Product"""
        return f'{self.prodid:<10} {self.desc:^40}'
        #  {self.quantity:^30} - {self.price:>30}'


class Attachment(Product):
    """Attachment class inherits basic information about parent product"""
    def __init__(self, prodid, materialtype, desc=str(), quantity=int(), price=int(), aid=int()):
        """Initializing Attachment with relevant information
        Creating getters and setters as well"""
        super().__init__(prodid, desc, quantity, price)
        self.materialtype = materialtype
        self.aid = aid

    @property
    def materialtype(self):
        return f'{self.__materialtype}'

    @materialtype.setter
    def materialtype(self, new_material):
        if new_material != '':
            self.__materialtype = new_material
        else:
            self.__materialtype = 'Unknown'

    @property
    def aid(self):
        return self.__aid

    @aid.setter
    def aid(self, new_aid):
        if new_aid != 0:
            self.__aid = new_aid
        else:
            self.__aid = 'Unknown'

    def __str__(self):
        return f'{self.prodid:<10} {self.desc:^40}'

