from tile import Tile

class TileUr(Tile):
    def __init__(self, id, pos, owner=None, special=False):
        self.id = id
        self.pos = pos
        self.owner = owner
        self.special = special
        self.occupant = None
    
    def get_state(self):
        state = {}
        state["id"] = self.id
        state["pos"] = self.pos
        state["owner"] = self.owner
        state["special"] = self.special
        state["occupant"] = self.occupant
        return state

    def get_owner(self):
        return self.owner

    def get_id(self):
        return self.id

    def get_pos(self):
        return self.pos

    def get_occupant(self):
        return self.occupant

    def set_occupant(self, occupant):
        self.occupant = occupant

    def is_occupied(self):
        return self.occupant is not None

    def is_empty(self):
        return self.occupant is None

    def is_special(self):
        return self.special
