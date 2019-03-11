from random import shuffle
import abc

# Iport objects
from dice_ur import DiceUr
from dice_set_ur import DiceSetUr
from token_ur import TokenUr
from agent_ur import AgentUr
from token_ur import TokenUr
from board_ur import BoardUr


class Engine:
    def __init__(self):
        # Generate the elements of the game
        self.players = (AgentUr(0), AgentUr(1))
        self.dices = DiceSetUr()
        self.board = BoardUr()
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
