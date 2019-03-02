from agent import Agent
from token_ur import TokenUr

class AgentUr(Agent):
    def __init__(self, id):
        self.id = id
        self.pieces = [TokenUr(i) for i in range(7)]

    def get_state(self):
        state = {}
        state["id"] = self.id
        state["pieces"] = self.pieces
        return state