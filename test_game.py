# test_game.py

import pytest
import pygame
from game import Game

def test_game_initialization():
    size = (5, 5)
    prob = 0.2
    game = Game(size, prob)
    assert game.board.size == size
    assert game.board.prob == prob
    assert game.sizeScreen == (800, 800)

def test_game_loadPictures():
    size = (5, 5)
    prob = 0.2
    game = Game(size, prob)
    game.loadPictures()
    assert 'empty-block' in game.images
    assert 'bomb-at-clicked-block' in game.images

def test_game_handleClick():
    size = (5, 5)
    prob = 0.2
    game = Game(size, prob)
    position = (100, 100)
    flag = False
    game.handleClick(position, flag)
    index = tuple(int(pos // size) for pos, size in zip(position, game.pieceSize))[::-1]
    piece = game.board.getPiece(index)
    assert piece.getClicked() == True
