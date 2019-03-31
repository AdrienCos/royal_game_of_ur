from dice_ur import DiceUr
from dice_set_ur import DiceSetUr
from pawn_ur import PawnUr
from agent_ur import AgentUr
from tile_ur import TileUr
from board_ur import BoardUr

die = DiceUr()
dice = DiceSetUr()
pawn = PawnUr(id=1)
agent = AgentUr(1)
tile = TileUr(1, 4, 1, True)
board = BoardUr()

# Test Dice methods
die.roll()
print(die.get_score())
print(die.get_values())

# Test DiceSet methods
dice.roll()
print(dice.get_score())
print(dice.get_values())
print(dice.get_dices())

# Test Pawn methods
print(pawn.get_id())
print(pawn.get_pos())
pawn.set_id(2)
pawn.set_pos(3)
print(pawn.get_id())
print(pawn.get_pos())

# Test Agent methods
print(agent.get_state())

# Test Tile methods
print(tile.get_state())
print(tile.get_owner())
print(tile.get_id())
print(tile.get_occupant())
print(tile.set_occupant(agent))
print(tile.get_owner())
print(tile.get_pos())
print(tile.is_empty())
print(tile.is_occupied())
print(tile.is_special())

# Test Board methods
print(board.get_state())
print(board.get_tiles())
board.set_occupant(0, 1)
print(board.get_state())