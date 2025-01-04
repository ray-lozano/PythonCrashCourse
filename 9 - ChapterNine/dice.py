import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        print(random.randint(1, self.sides))

    def roll_ten_side(self):
        self.sides = 10
        print(random.randint(1, self.sides))

    def roll_twenty_side(self):
        self.sides = 20
        print(random.randint(1, self.sides))

dice = Die()
for x in range(1, 11):
    dice.roll_twenty_side()

