# board.py
from piece import Piece
import random

class Board:
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
        self.board = [[Piece(random.random() < prob) for _ in range(size[1])] for _ in range(size[0])]
        self.setNeighbors()
        self.won = False
        self.lost = False

    def setNeighbors(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                piece = self.board[row][col]
                neighbors = []
                self.addToNeighborsList(neighbors, row, col)
                piece.setNeighbors(neighbors)

    def addToNeighborsList(self, neighbors, row, col):
        for r in range(max(0, row - 1), min(row + 2, len(self.board))):
            for c in range(max(0, col - 1), min(col + 2, len(self.board[0]))):
                if r == row and c == col:
                    continue
                neighbors.append(self.board[r][c])

    def getBoard(self):
        return self.board

    def getPiece(self, index):
        return self.board[index[0]][index[1]]

    def handleClick(self, piece, flag):
        if flag:
            piece.flag()
        else:
            piece.click()

    def getWon(self):
        return self.won

    def getLost(self):
        return self.lost
