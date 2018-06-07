import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *

# Dict mapping the board position ot the board coordinates for Player 0 
# pos_to_coords_P0 = {
#     0: 
# }

class Piece(pygame.Rect):
    def __init__(self, x, y, size, player):
        pygame.Rect.__init__(self, x, y, size, size)
        self.start_x = x
        self.start_y = y
        self.cx = round(x + size / 2)
        self.cy = round(y + size / 2)
        self.radius = int(size / 2)
        if player == 0:
            self.color = P0COLOR
        else:
            self.color = P1COLOR
        self.pos = -1
        self.player = player
    
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

    def reset_pos(self):
        self.pos = -1
        # pygame.Rect.left = self.start_x
        # pygame.Rect.top = self.start_y

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
