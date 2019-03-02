import abc


class Agent(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_state(self):
        # Get the state of all the elements belonging to the agent
        # Should return a dict
        pass
