from dice import Dice
from random import shuffle


class DiceUr(Dice):
    def __init__(self):
        self.values = [0, 0, 1, 1]

    def roll(self):
        shuffle(self.values)

    def get_score(self):
        return self.values[0]

    def get_values(self):
        return self.values
