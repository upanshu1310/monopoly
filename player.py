class Player:
    def __init__(self, name, colour=None):
        self.name = name
        self.colour = colour
        self.balance = 15000
        self.transactions = []
    
    def __str__(self):
        return f'{self.name} ${self.balance}'

    def transfer(self, player, amount):
        self.balance -= amount
        player.balance += amount
    
    def spend(self, amount):
        self.balance -= amount

    def collect(self, amount):
        self.balance += amount
    
    def getBalance(self):
        return self.balance