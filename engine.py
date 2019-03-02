from random import shuffle
import abc

# Iport objects
from dice_ur import DiceUr
from dice_set_ur import DiceSetUr
from token_ur import TokenUr
from agent_ur import AgentUr
from token_ur import TokenUr


# class Tile:
#     def __init__(self, pos, player_id, safe, tile_id):
#         # Generate the tile
#         self.safe = safe
#         self.player_id = player_id
#         self.pos = pos
#         self.occupant = None
#         self.id = tile_id

#     def get_player_id(self):
#         # Return the player ID (None if the tile is not player-specific)
#         return self.player_id

#     def get_tile_id(self):
#         # Return the ID of the tile
#         return self.id

#     def get_pos(self):
#         # Return the position of the tile (from 0 to 13)
#         return self.pos

#     def set_occupant(self, occupant):
#         # Set the occupant of the tile (an instance of Piece)
#         self.occupant = occupant

#     def get_occupant(self):
#         # Return the occupand of the tile (an instance of Piece)
#         return self.occupant

#     def is_occupied(self):
#         # Return True if there is a piece here, False otherwise
#         return self.occupant is not None

#     def is_empty(self):
#         # Return True if no piece is here
#         return self.occupant is None

#     def is_safe(self):
#         # Return True if the tile is a safe one
#         return self.is_safe


class Board:
    def __init__(self):
        # Generate the board
        self.tiles = []
        self.create_tiles()

    def create_tiles(self):
        for i in range(1, 5):
            new_tile = TileUr(i, i, 0, False)
            self.tiles.append(new_tile)
            new_tile = TileUr(i+5, i, 1, False)
            self.tiles.append(new_tile)
        for i in range(5, 13):
            new_tile = TileUr(i+5, i, None, False)
            self.tiles.append(new_tile)
        for i in range(13, 15):
            new_tile = TileUr(i+5, i, 0, False)
            self.tiles.append(new_tile)
            new_tile = TileUr(i+9, i, 1, False)
            self.tiles.append(new_tile)
        for tile in self.tiles:
            if tile.get_pos() in [4, 8, 14]:
                tile.safe = True

    def get_tiles(self):
        return self.tiles

    def set_tile_occupant(self, tile_id, occupant):
        for tile in self.tiles:
            if tile.get_id() == tile_id:
                tile.set_occupant(occupant)

    def get_pos_from_id(self, tile_id):
        # Return the postion of the tile linked to the given id
        for tile in self.tiles:
            if tile.get_id() == tile_id:
                return tile.get_pos()

    def get_tile_from_id(self, tile_id):
        # Return the tile linked to the given id
        for tile in self.tiles:
            if tile.get_id() == tile_id:
                return tile


class Engine:
    def __init__(self):
        # Generate the elements of the game
        self.players = (AgentUr(0), AgentUr(1))
        self.dices = DiceSetUr()
        self.board = Board()
        self.state = "Throw"
        self.activePlayer = 0

    def throw_dices(self):
        # Throws the dices if the state is currently in "Throw"
        if self.state == "Throw":
            self.dices.roll()
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
                valid.append(tile.get_id())
        return valid

    def is_reachable(self, tile, piece):
        # Return True if the piece is the correct distance from the tile (based on the dices value),
        # and the tile and the piece are compatible player-wise
        distance = piece.get_pos() + self.get_dices_score() - tile.get_pos()
        if distance == 0:
            if tile.get_owner() == None or tile.get_owner() == self.activePlayer:
                return True
        return False

    def is_vulnerable(self, tile):
        # Return True if the tile can be taken by the current player, regardless of piece
        is_empty = tile.is_empty()
        is_safe = tile.is_special()
        is_same_team = (tile.get_owner() == self.activePlayer)
        if is_empty:
            return True
        elif is_safe or is_same_team:
            return False
        else:
            return True
