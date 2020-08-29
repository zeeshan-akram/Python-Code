import random


class Dice:
    def roll(self):
        number = (random.randint(0, 9), random.randint(0, 9))
        print(number)


x = Dice()
x.roll()