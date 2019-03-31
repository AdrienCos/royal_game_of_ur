from pawn import Pawn

class PawnUr(Pawn):
    def __init__(self, id):
        self.pos = 0
        self.id = id
    
    def get_state(self):
        state = {}
        state["id"] = self.id
        state["pos"] = self.pos
        return state

    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos
    
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

