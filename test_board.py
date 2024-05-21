# test_board.py
import pytest
from board import Board

def test_board_initialization():
    size = (5, 5)
    prob = 0.2
    board = Board(size, prob)
    assert len(board.getBoard()) == size[0]
    assert len(board.getBoard()[0]) == size[1]

def test_board_click():
    size = (5, 5)
    prob = 0.2
    board = Board(size, prob)
    piece = board.getPiece((0, 0))
    board.handleClick(piece, flag=False)
    assert piece.getClicked() == True

def test_board_flag():
    size = (5, 5)
    prob = 0.2
    board = Board(size, prob)
    piece = board.getPiece((0, 0))
    board.handleClick(piece, flag=True)
    assert piece.getFlagged() == True
    board.handleClick(piece, flag=True)
    assert piece.getFlagged() == False
