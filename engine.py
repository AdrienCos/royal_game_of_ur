from constants import *
from random import shuffle

class Dice:
    def __init__(self):
        # Create the array of the values of the dice
        self.values = [0, 0, 1, 1]
    def throw(self):
        # Shuffle the values
        shuffle(self.values)
    def getValue(self):
        # Returnt the first ("top") value of the dice
        return self.values[0]

class DiceSet:
    def __init__(self):
        # Generate the dices
        self.dices = [Dice() for i in range(4)]
    def throw(self):
        # Throw every dice
        for dice in self.dices:
            dice.throw()
    def getScore(self):
        # Add the value of each dice and return it
        score = 0
        for dice in self.dices:
            score += dice.getValue()
        return score

class Piece:
    def __init__(self, piece_id):
        # create the piece
        self.id = piece_id
        self.pos = 0
    def getPos(self):
        # Return the current position of the piece
        return self.pos
    def setPos(self, new_pos):
        # Set the new posistion of the piece
        self.pos = new_pos

class Player:
    def __init__(self, player_id):
        # Generate the pieces
        self.id = player_id
        self.pieces = [Piece(i) for i in range(7)]
    def getPiecesPos(self):
        # Get the position of every pieces and return it
        pos = [piece.getPos() for piece in self.pieces]
        return pos
    def movePiece(self, piece_id, pos):
        # Move the desired piece to the specified position
        self.pieces[piece_id].setPos(pos)


class Engine:
    def __init__(self):
        # Generate the elements of the game
        self.players = (Player(0), Player(1))
        self.dices = DiceSet()
        self.board = Board()
        self.state = "Throw"
        self.activePlayer = 0

    def throwDices(self):
        if self.state == "Throw":
            self.dices.throw()
            self.state = "Move"

    def getDicesScore(self):
        self.dices.getScore()



