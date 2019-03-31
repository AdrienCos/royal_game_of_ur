from agent import Agent
from pawn_ur import PawnUr

class AgentUr(Agent):
    def __init__(self, id):
        self.id = id
        self.pieces = [PawnUr(i) for i in range(7)]

    def get_state(self):
        state = {}
        state["id"] = self.id
        state["pieces"] = self.pieces
        return state