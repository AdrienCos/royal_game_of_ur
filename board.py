import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *

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