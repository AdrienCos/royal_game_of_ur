import abc


class Dice(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def roll(self):
        pass

    @abc.abstractmethod
    def get_score(self):
        pass

    @abc.abstractmethod
    def get_values(self):
        pass
