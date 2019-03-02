from dice_ur import DiceUr
from dice_set_ur import DiceSetUr
from token_ur import TokenUr
from agent_ur import AgentUr
from tile_ur import TileUr

die = DiceUr()
dice = DiceSetUr()
token = TokenUr(id=1)
agent = AgentUr(1)
tile = TileUr(1, 4, 1, True)

# Test Dice methods
die.roll()
print(die.get_score())
print(die.get_values())

# Test DiceSet methods
dice.roll()
print(dice.get_score())
print(dice.get_values())
print(dice.get_dices())

# Test Token methods
print(token.get_id())
print(token.get_pos())
token.set_id(2)
token.set_pos(3)
print(token.get_id())
print(token.get_pos())

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