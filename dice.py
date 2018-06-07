import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *

class Dice(pygame.Rect):
    def __init__(self, x, y, size):
        pygame.Rect.__init__(self, x, y, size, size)
        self.vertices = [(x + DICESIZE/2, y), (x, y + DICESIZE), (x + DICESIZE, y + DICESIZE)]
        self.color = DICECOLOR
        self.values = [0, 0, 1, 1]
        self.dots = [
            (round(x + DICESIZE/2), round(y + 2*DICESIZE/3)),
            (round(x + DICESIZE/2), round(y)),
            (round(x), round(y + DICESIZE)),
            (round(x + DICESIZE), round(y + DICESIZE))
        ]
            
    def throw(self):
        shuffle(self.values)
    
    def get_value(self):
        return self.values[0]

    def get_values(self):
        return self.values

    def get_color(self):
        return self.color

    def get_vertices(self):
        return self.vertices

    def get_dots(self):
        dots = []
        for i, value in enumerate(self.values):
            if value == 1:
                dots.append([self.dots[i], DOTSIZE, DOTCOLOR])
        return dots

class DiceSet:
    def __init__(self):
        self.dices = []
        x_pos = XOFFSET + (8 * TILESIZE + 9 * TILESPACING) + 0.5 * DICESIZE
        for i in range(4):
            y_pos = YOFFSET + i * DICESIZE +  (2 * TILESPACING + TILESIZE) * i / 3
            new_dice = Dice(x_pos, y_pos, DICESIZE)
            self.dices.append(new_dice)
    
    def get_dices(self):
        return self.dices
    
    def throw(self):
        for dice in self.dices:
            dice.throw()
    
    def get_score(self):
        score = 0
        for dice in self.dices:
            score += dice.get_value()
        return score
