# State

Add a `State` class, that contains all the elements of the game's state (pieces and state variables). Its methods provide detailed informations about the game state (e.g. `is_finished`, `get_legal_actions`, `get_successor`). It also povides a `deepcopy` method to allow for speculative planning.

# Actions

Create an `Actions` class that only implements `@staticmethod` methods, that each correspond to an action. They take various arguments and return the result of the application of this action to these elements (e.g. `get_legal_actions` takes a `Piece` and a `Board` and return a list of all acesible `Tiles`)

# Rules

Create a `Rules` class, that only implements `@staticmethod` methods. These methods take a `State` (and optionally an `Action`) as argument, and act on the `State` or return an `Action` 