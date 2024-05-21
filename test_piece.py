# test_piece.py

import pytest
from piece import Piece

def test_piece_initialization():
    piece = Piece(hasBomb=True)
    assert piece.getHasBomb() == True
    assert piece.getClicked() == False
    assert piece.getFlagged() == False

def test_piece_click():
    piece = Piece(hasBomb=False)
    piece.click()
    assert piece.getClicked() == True

def test_piece_flag():
    piece = Piece(hasBomb=False)
    piece.flag()
    assert piece.getFlagged() == True
    piece.flag()
    assert piece.getFlagged() == False
