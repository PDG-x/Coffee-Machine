
class Beverage: # We create out beverahe class, we are going to set all the attributes in a dictionary inside the menu class.
    def __init__(self, name, variant, size, price, milk = None, milk_type = None, sugar = None, decor = None):
        self.name = name
        self.variant = variant
        self.size = size
        self.price = price
        self.milk = milk
        self.milk_type = milk_type # we need a milk_type object in order to specify the different milk types for the customer
        self.sugar = sugar
        self.decor = decor
