#!/usr/bin/python3

from engine import *

player = Player(1)
player.getPiecesPos()
player.movePiece(0, 3)
print(player.getPiecesPos())

dices = DiceSet()
dices.throw()
print(dices.getScore())
