
class Product:
    def __init__(self, name):
        self.name = name
        self.price=0

    def __str__(self):
        return self.name

    def setPrice (self,price):
        self.price=price