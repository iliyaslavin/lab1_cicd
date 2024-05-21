# piece.py
class Piece:
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False

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
