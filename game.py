import pygame, time
from pygame.locals import *
from random import shuffle

from dice import *
from board import *
from player import *
from constants import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = WINWIDTH, WINHEIGHT
        self.clock = pygame.time.Clock()
        self.game_steps = {0:"throw", 1:"move", 2:""}
        

    def on_init(self):
        # Initiate the pygame engine
        pygame.init()
        # Ban the MouseMotion and ActiveEvent events
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.ACTIVEEVENT)
        # Initiate the drawing surface
        self._display_surf = pygame.display.set_mode(self.size)
        # Set the game as running
        self._running = True
        self.clicked_tiles = []
        # Create the board and players and dices
        self.board = Board()
        self.players = [Player(0), Player(1)]
        self.dices = DiceSet()
        self.current_step = 0

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # If a tile is clicked, color it red
            for tile in self.board.get_tiles():
                if tile.collidepoint(mouse_pos):
                    tile.set_color(RED)
                    self.clicked_tiles.append(tile)
            # If a dice is clicked, throw the dice
            for dice in self.dices.get_dices():
                if dice.collidepoint(mouse_pos):
                    self.dices.throw()
        # Reset the color of all clicked tiles when the mouse is released
        if event.type == pygame.MOUSEBUTTONUP:
            for tile in self.clicked_tiles:
                tile.reset_color()
            self.clicked_tiles = []
        # Exit the game
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        # Cap the framerate
        delta = self.clock.tick(MAXFPS)
        print(self.dices.get_score())

    def on_render(self):
        # Draw the background
        self._display_surf.fill(BGCOLOR)
        # Draw the borders of the tiles
        for border in self.board.get_borders():
            pygame.draw.rect(self._display_surf, border.get_color(), border)
        # Draw the tiles
        for tile in self.board.get_tiles():
            pygame.draw.rect(self._display_surf, tile.get_color(), tile)
        # Draw the pieces
        for player in self.players:
            for piece in player.get_pieces():
                pygame.draw.circle(self._display_surf, piece.get_color(), (piece.x, piece.y), piece.radius)
        # Draw the dices
        for dice in self.dices.get_dices():
            pygame.draw.polygon(self._display_surf, dice.get_color(), dice.get_vertices())
            for dot in dice.get_dots():
                pygame.draw.circle(self._display_surf, dot[2], dot[0], dot[1])
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                # print(event)
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
