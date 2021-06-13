
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.price=0
        self.amount = 0

    def __str__(self):
        return self.name

    def setPrice (self,price):
        self.price=price
