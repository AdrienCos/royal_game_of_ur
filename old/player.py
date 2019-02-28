import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *

# Dict mapping the board position ot the board coordinates for Player 0 
pos_to_coords = {0:{
    0:  (XOFFSET + 3*TILESIZE + 3*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE),
    1:  (XOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE),
    2:  (XOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE),
    3:  (XOFFSET + 0*TILESIZE + 0*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE),
    4:  (XOFFSET + 0*TILESIZE + 0*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    5:  (XOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    6:  (XOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    7:  (XOFFSET + 3*TILESIZE + 3*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    8:  (XOFFSET + 4*TILESIZE + 4*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    9:  (XOFFSET + 5*TILESIZE + 5*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    10: (XOFFSET + 6*TILESIZE + 6*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    11: (XOFFSET + 7*TILESIZE + 7*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    12: (XOFFSET + 7*TILESIZE + 7*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE),
    13: (XOFFSET + 6*TILESIZE + 6*TILESPACING + 0.5*PIECESIZE, YOFFSET + 0.5*PIECESIZE)
}, 
1:{
    0:  (XOFFSET + 3*TILESIZE + 3*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE),
    1:  (XOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE),
    2:  (XOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE),
    3:  (XOFFSET + 0*TILESIZE + 0*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE),
    4:  (XOFFSET + 0*TILESIZE + 0*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    5:  (XOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    6:  (XOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    7:  (XOFFSET + 3*TILESIZE + 3*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    8:  (XOFFSET + 4*TILESIZE + 4*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    9:  (XOFFSET + 5*TILESIZE + 5*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    10: (XOFFSET + 6*TILESIZE + 6*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    11: (XOFFSET + 7*TILESIZE + 7*TILESPACING + 0.5*PIECESIZE, YOFFSET + 1*TILESIZE + 1*TILESPACING + 0.5*PIECESIZE),
    12: (XOFFSET + 7*TILESIZE + 7*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE),
    13: (XOFFSET + 6*TILESIZE + 6*TILESPACING + 0.5*PIECESIZE, YOFFSET + 2*TILESIZE + 2*TILESPACING + 0.5*PIECESIZE)
}}

class Piece(pygame.Rect):
    def __init__(self, x, y, size, player):
        pygame.Rect.__init__(self, x, y, size, size)
        self.start_x = x
        self.start_y = y
        self.radius = round(size / 2)
        self.cx = round(x + self.radius)
        self.cy = round(y + self.radius)
        if player == 0:
            self.color = P0COLOR
        else:
            self.color = P1COLOR
        self.pos = -1
        self.player = player
        print(self.left)
    
    def get_player(self):
        return self.player
    
    def get_color(self):
        return self.color

    def is_double(self):
        """The piece is on any doubling tile"""
        return self.pos == 3 or self.pos == 7 or self.pos == 13

    def is_safe(self):
        """The piece is on the center safe tile"""
        return self.pos == 7

    def is_private(self):
        """The piece is in the player's private section"""
        return self.pos <= 3 or self.pos >= 13
    
    def on_board(self):
        return self.pos != -1 and self.pos != 14

    def is_finished(self):
        return self.pos == 14

    def is_valid_move(self, value):
        if self.is_finished():
            return False
        if self.pos + value > 14:
            return False
        return True
    
    def get_pos(self):
        return self.pos

    def add_pos(self, value):
        self.pos += value
        if self.pos < 14:
            self.x, self.y = pos_to_coords[self.player][self.pos]
            self.cx = round(self.x + self.radius)
            self.cy = round(self.y + self.radius)
        else:
            self.x = self.start_x + 4 * (TILESIZE + TILESPACING)
            self.y = self.start_y
            self.cx = round(self.x + self.radius)
            self.cy = round(self.y + self.radius)

    def reset_pos(self):
        self.pos = -1
        self.x, self.y = self.start_x, self.start_y
        self.cx = round(self.x + self.radius)
        self.cy = round(self.y + self.radius)

class Player:
    def __init__(self, player):
        self.player = player
        self.pieces = []
        for col in range(7):
            x_pos = XOFFSET + (col * (1.5 * PIECESIZE)) - TILESPACING
            if self.player == 0:
                y_pos = YOFFSET - 2 * PIECESIZE - TILESPACING
            else:
                y_pos = YOFFSET + 3 * TILESIZE + 3 * TILESPACING + 1 * PIECESIZE
            new_piece = Piece(x_pos, y_pos, PIECESIZE, self.player)
            self.pieces.append(new_piece)
    
    def get_player(self):
        return self.player

    def get_pieces(self):
        return self.pieces

    def get_safe_pieces(self):
        return [piece for piece in self.pieces if piece.is_safe()]

    def get_unsafe_pieces(self):
        return [piece for piece in self.pieces if not piece.is_safe()]
