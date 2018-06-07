import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *
from player import *

class Tile(pygame.Rect):
    def __init__(self, x, y, size, is_safe):
        pygame.Rect.__init__(self, x, y, size, size)
        if is_safe:
            self.color = SAFE_TILE
            self.default_color = SAFE_TILE
        else:
            self.color = UNSAFE_TILE
            self.default_color = UNSAFE_TILE
        self.is_safe = is_safe

    def safe(self):
        return self.is_safe
        
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def reset_color(self):
        self.color = self.default_color

class Border(pygame.Rect):
    def __init__(self, x, y, size):
        pygame.Rect.__init__(self, x, y, size, size)
        self.color = BORDERCOLOR
        self.default_color = BORDERCOLOR
        
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
    
    def reset_color(self):
        self.color = self.default_color

class Board:
    def __init__(self):
        self.tiles = []
        self.borders = []
        for row in range(3):
            for col in range(8):
                # Do not generate tiles that are not supposed to exist
                if not (row in [0, 2] and col in [4, 5]):
                    if [row, col] in [[0, 0], [2, 0], [1, 3], [0, 6], [2, 6]]:
                        is_safe = True
                    else:
                        is_safe = False
                    x_pos = XOFFSET + col * (TILESIZE + TILESPACING)
                    y_pos = YOFFSET + row * (TILESIZE + TILESPACING)
                    new_tile = Tile(x_pos, y_pos, TILESIZE, is_safe)
                    self.tiles.append(new_tile)

                    x_pos -= TILESPACING
                    y_pos -= TILESPACING
                    new_border = Border(x_pos, y_pos, TILESIZE + 2 * TILESPACING)
                    self.borders.append(new_border)

    def get_tiles(self):
        return self.tiles

    def get_borders(self):
        return self.borders

    def is_valid_move(self, piece, players, value):
        """Returns True if the piece can move by the current dice value, 
        and False otherwise"""
        # If the piece is already finished or would exceed the maximum position
        if not piece.is_valid_move(value):
            print("Move not valid: out-of-bound")
            return False
        target_pos = piece.get_pos() + value
        current_player = piece.get_player()
        # If the target tile is already occupied by another piece of the same player
        for other_piece in players[current_player].get_pieces():
            if other_piece.get_pos() == target_pos:
                print("Move not valid: tile occupied by allied piece")
                return False
        # If the target tile is safe and occupied by another piece of the other player
        for other_piece in players[1 - current_player].get_pieces():
            if other_piece.get_pos() == target_pos and other_piece.is_safe():
                print("Move not valid: safe tile occupied by adversary")
                return False
        # If the move is valid
        return True