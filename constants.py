# Define the colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SAFE_TILE = (242, 187, 9)       # Orange
UNSAFE_TILE = (66, 160, 255)    # Blue
BORDERCOLOR = (206, 206, 206)   # Light gray
BGCOLOR = (255, 235, 173)       # Pale yellow
P0COLOR = (0, 0, 0)             # Black
P1COLOR = (255, 255, 255)       # White
DICECOLOR = (76, 76, 76)        # Dark gray
DOTCOLOR = (255, 255, 255)      # White

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

# Compute the size of a dice and a dice dot
DICESIZE = 0.5 * TILESIZE
DOTSIZE = round(0.1 * DICESIZE)