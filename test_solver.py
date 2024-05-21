# test_solver.py

import pytest
from board import Board
from solver import Solver

def test_solver_initialization():
    size = (5, 5)
    prob = 0.2
    board = Board(size, prob)
    solver = Solver(board)
    assert solver.board == board

def test_solver_move():
    size = (5, 5)
    prob = 0.2
    board = Board(size, prob)
    solver = Solver(board)
    solver.move()  # Assuming move method modifies the board
    # Here you should add specific assertions depending on what move() does
