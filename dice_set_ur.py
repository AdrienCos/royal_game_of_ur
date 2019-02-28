import abc

# Import objects
from dice_ur import DiceUr
from dice_set import DiceSet

class DiceSetUr(DiceSet):
    def __init__(self):
        self.dices = [DiceUr() for i in range(4)]
        pass

    def roll(self):
        for dice in self.dices:
            dice.roll()
        pass

    def get_score(self):
        score = 0
        for dice in self.dices:
            score += dice.get_score()
        return score

    def get_values(self):
        values = []
        for dice in self.dices:
            values.append(dice.get_score())
        return values

    def get_dices(self):
        dices = []
        for dice in self.dices:
            dices.append(dice.get_values())
        return dices