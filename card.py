class Card: # We create our class Card
    def __init__(self, id, user_type, name, balance): # We set the attributes. In order to match with our csv file.
        self.id = id
        self.user_type = user_type
        self.name = name
        self.balance = float(balance)   #the balance object is used to later subtract coffee price from the card amount

    def pay(self, amount):
        self.balance -= float(amount)   #the pay funtion takes the balance in order in order to subtract the coffee price
