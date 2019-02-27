#!/usr/bin/python3

from engine import *


engine = Engine()

engine.throw_dices()
score = engine.get_dices_score()

piece = engine.players[0].pieces[0]
valid_tiles = engine.get_valid_tiles(piece)

print(score, valid_tiles)
for tile_id in valid_tiles:
    print(engine.board.get_tile_from_id(tile_id))

