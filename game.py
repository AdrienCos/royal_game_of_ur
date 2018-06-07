import pygame, time
from pygame.locals import *

# Define the colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SAFE_TILE = (242, 187, 9)       # Orange
UNSAFE_TILE = (66, 160, 255)    # Blue
BORDERCOLOR = (206, 206, 206)   # Light gray
BGCOLOR = (255, 235, 173)       # Pale yellow
P0COLOR = (0, 0, 0)             # White
P1COLOR = (255, 255, 255)       # Black

# Define the max FPS
MAXFPS = 60

# Define the game window size
WINWIDTH = 800
WINHEIGHT = 600

# Compute the size, spacing and positions of the tiles
TILESIZE = min(WINWIDTH/13, WINHEIGHT/8)
TILESPACING = TILESIZE / 5
XOFFSET = (WINWIDTH - (8 * TILESIZE + 7 * TILESPACING)) / 2
YOFFSET = (WINHEIGHT - (3 * TILESIZE + 2 * TILESPACING)) / 2

# Compute the size of the player pieces
PIECESIZE = 0.5 * TILESIZE

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
                y_pos = YOFFSET - 1.5 * PIECESIZE
            else:
                y_pos = YOFFSET + 3 * TILESIZE + 4 * TILESPACING + 0.5 * PIECESIZE
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

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = WINWIDTH, WINHEIGHT
        self.clock = pygame.time.Clock()
        self.clicked_tiles = []
        self.to_render = []

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._running = True
        self._display_surf.fill(BGCOLOR)
        self.tiles, self.borders = self.create_board()
        for border in self.borders:
            pygame.draw.rect(self._display_surf, border.get_color(), border)
            self.to_render.append(border.copy())
        for tile in self.tiles:
            pygame.draw.rect(self._display_surf, tile.get_color(), tile)
            self.to_render.append(tile.copy())
        self.players = [Player(0), Player(1)]
        for player in self.players:
            for piece in player.get_pieces():
                pygame.draw.circle(self._display_surf, piece.get_color(), (piece.x, piece.y), piece.radius)
                self.to_render.append(piece.copy())


        pygame.display.update()

    def create_board(self):
        tiles = []
        borders = []
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
                    tiles.append(new_tile)

                    x_pos -= TILESPACING
                    y_pos -= TILESPACING
                    new_border = Border(x_pos, y_pos, TILESIZE + 2 * TILESPACING)
                    borders.append(new_border)
        return tiles, borders

    def on_event(self, event):
        # If a tile is cliked, color it red
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for tile in self.tiles:
                if tile.collidepoint(mouse_pos):
                    tile.set_color(RED)
                    pygame.draw.rect(self._display_surf, tile.get_color(), tile)
                    self.to_render.append(tile)
                    self.clicked_tiles.append(tile)
        # Reset the color of all clicked tiles
        if event.type == pygame.MOUSEBUTTONUP:
            for tile in self.clicked_tiles:
                tile.reset_color()
                pygame.draw.rect(self._display_surf, tile.get_color(), tile)
                self.to_render.append(tile)
            self.clicked_tiles = []
        # Exit the game
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        # Cap the framerate
        delta = self.clock.tick(MAXFPS)
        # Render all tiles and borders again by default
        # TODO: Only render tiles that need it
        # for border in self.borders:
        #     pygame.draw.rect(self._display_surf, border.get_color(), border)
        #     self.to_render.append(border.copy())
        # for tile in self.tiles:
        #     pygame.draw.rect(self._display_surf, tile.get_color(), tile)
        #     self.to_render.append(tile.copy())

    def on_render(self):
        print(self.to_render)
        pygame.display.update(self.to_render)
        self.to_render = []

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
