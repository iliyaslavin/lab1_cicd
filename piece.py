# piece.py
class Piece:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def click(self):
        self.clicked = True

    def flag(self):
        self.flagged = not self.flagged

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    def getNeighbors(self):
        return self.neighbors
