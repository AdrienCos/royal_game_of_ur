import abc


class Token(abc.ABC):
    @abc.abstractmethod
    def __init__(self, id=0, pos=0):
        pass

    @abc.abstractmethod
    def get_state(self):
        pass

    @abc.abstractmethod
    def get_pos(self):
        pass

    @abc.abstractmethod
    def set_pos(self, pos):
        pass

    @abc.abstractmethod
    def get_id(self):
        pass

    @abc.abstractmethod
    def set_id(self, id):
        pass
    
