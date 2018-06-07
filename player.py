import pygame, time
from pygame.locals import *
from random import shuffle
from constants import *

class Piece(pygame.Rect):
    def __init__(self, x, y, size, player):
        pygame.Rect.__init__(self, x, y, size, size)
        self.start_x = x
        self.start_y = y
        self.radius = int(size / 2)
        if player == 0:
            self.color = P0COLOR
        else:
            self.color = P1COLOR
        self.player = player
        self.safe = False
        self.on_board = False
        self.finished = False
    
    def get_player(self):
        return self.player
    
    def get_color(self):
        return self.color

    def is_safe(self):
        return self.safe
    
    def on_board(self):
        return self.on_board

    def is_finished(self):
        return self.finished

    def reset_pos(self):
        pygame.Rect.left = self.start_x
        pygame.Rect.top = self.start_y

class Player:
    def __init__(self, player):
        self.player = player
        self.pieces = []
        for col in range(7):
            x_pos = XOFFSET + (col * (1.5 * PIECESIZE))
            if self.player == 0:
                y_pos = YOFFSET - 2 * PIECESIZE
            else:
                y_pos = YOFFSET + 3 * TILESIZE + 4 * TILESPACING + 1 * PIECESIZE
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
