from board import Board
from tile_ur import TileUr

class BoardUr(Board):
    def __init__(self):
        self.tiles = []
        self.create_tiles()

    def get_state(self):
        state = {}
        for tile in self.tiles:
            id = tile.get_id()
            state[id] = tile.get_state()
        return state

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

    def set_occupant(self, id, player_id):
        for tile in self.tiles:
            if id == tile.get_id():
                tile.set_occupant(player_id)

    def get_tiles(self):
        return self.tiles