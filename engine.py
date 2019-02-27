from constants import *
from random import shuffle

# Symbolic constants
EMPTY = 0


class Dice:
    def __init__(self):
        # Create the array of the values of the dice
        self.values = [0, 0, 1, 1]

    def throw(self):
        # Shuffle the values
        shuffle(self.values)

    def get_value(self):
        # Return the first ("top") value of the dice
        return self.values[0]


class DiceSet:
    def __init__(self, dice_nb):
        # Generate the dices
        self.dices = [Dice() for i in range(dice_nb)]

    def throw(self):
        # Throw every dice
        for dice in self.dices:
            dice.throw()

    def get_score(self):
        # Add the value of each dice and return it
        score = 0
        for dice in self.dices:
            score += dice.get_value()
        return score


class Piece:
    def __init__(self, piece_id):
        # create the piece
        self.id = piece_id
        self.pos = 0

    def get_pos(self):
        # Return the current position of the piece
        return self.pos

    def set_pos(self, new_pos):
        # Set the new posistion of the piece
        self.pos = new_pos

    def get_piece_id(self):
        # Return the ID of the piece
        return self.id


class Player:
    def __init__(self, player_id):
        # Generate the pieces
        self.id = player_id
        self.pieces = [Piece(i) for i in range(7)]

    def get_pieces_pos(self):
        # Get the position of every pieces and return it
        pos = [piece.getPos() for piece in self.pieces]
        return pos

    def move_piece(self, piece_id, pos):
        # Move the desired piece to the specified position
        self.pieces[piece_id].setPos(pos)

    def get_player_id(self):
        return self.id


class Tile:
    def __init__(self, pos, player_id, safe, tile_id):
        # Generate the tile
        self.safe = safe
        self.player_id = player_id
        self.pos = pos
        self.occupant = None
        self.id = tile_id

    def get_player_id(self):
        # Return the player ID (None if the tile is not player-specific)
        return self.player_id

    def get_tile_id(self):
        # Return the ID of the tile
        return self.id

    def get_pos(self):
        # Return the position of the tile (from 0 to 13)
        return self.pos

    def set_occupant(self, occupant):
        # Set the occupant of the tile (an instance of Piece)
        self.occupant = occupant

    def get_occupant(self):
        # Return the occupand of the tile (an instance of Piece)
        return self.occupant

    def is_occupied(self):
        # Return True if there is a piece here, False otherwise
        return self.occupant is not None

    def is_empty(self):
        # Return True if no piece is here
        return self.occupant is None

    def is_safe(self):
        # Return True if the tile is a safe one
        return self.is_safe


class Board:
    def __init__(self):
        # Generate the board
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        for i in range(1, 5):
            new_tile = Tile(i, 0, False, i)
            self.tiles.append(new_tile)
            new_tile = Tile(i, 1, False, i+5)
            self.tiles.append(new_tile)
        for i in range(5, 13):
            new_tile = Tile(i, None, False, i+5)
            self.tiles.append(new_tile)
        for i in range(13, 15):
            new_tile = Tile(i, 0, False, i+5)
            self.tiles.append(new_tile)
            new_tile = Tile(i, 1, False, i+9)
            self.tiles.append(new_tile)
        for tile in self.tiles:
            if tile.get_pos() in [4, 8, 14]:
                tile.safe = True

    def get_tiles(self):
        return self.tiles

    def set_tile_occupant(self, tile_id, occupant):
        for tile in self.tiles:
            if tile.get_tile_id() == tile_id:
                tile.set_occupant(occupant)
    
    def get_pos_from_id(self, tile_id):
        # Return the postion of the tile linked to the given id
        for tile in self.tiles:
            if tile.get_tile_id() == tile_id:
                return tile.get_pos()

    def get_tile_from_id(self, tile_id):
        # Return the tile linked to the given id
        for tile in self.tiles:
            if tile.get_tile_id() == tile_id:
                return tile


class Engine:
    def __init__(self):
        # Generate the elements of the game
        self.players = (Player(0), Player(1))
        self.dices = DiceSet(4)
        self.board = Board()
        self.state = "Throw"
        self.activePlayer = 0

    def throw_dices(self):
        # Throws the dices if the state is currently in "Throw"
        if self.state == "Throw":
            self.dices.throw()
            self.state = "Move"

    def get_dices_score(self):
        # Returns the current dices score
        return self.dices.get_score()

    def get_valid_tiles(self, piece):
        # Returns a list of tile IDs that the selected piece can reach
        tiles = self.board.get_tiles()
        valid = []
        for tile in tiles:
            if self.is_reachable(tile, piece) and self.is_vulnerable(tile):
                valid.append(tile.get_tile_id())
        return valid

    def is_reachable(self, tile, piece):
        # Return True if the piece is the correct distance from the tile (based on the dices value),
        # and the tile and the piece are compatible player-wise
        distance = piece.get_pos() + self.get_dices_score() - tile.get_pos()
        if distance == 0:
            if tile.get_player_id() == None or tile.get_player_id() == self.activePlayer:
                return True
        return False
    
    def is_vulnerable(self, tile):
        # Return True if the tile can be taken by the current player, regardless of piece
        is_empty = tile.is_empty()
        is_safe = tile.is_safe()
        is_same_team = (tile.get_player_id() == self.activePlayer)
        if is_empty:
            return True
        elif is_safe or is_same_team:
            return False
        else:
            return True