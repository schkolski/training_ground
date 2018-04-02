import unittest

from attacking_queens.board import ChessBoard
from attacking_queens.board import BlackQueen
from attacking_queens.exceptions import BadQueenPlacementException


class PlacingQueensTests(unittest.TestCase):

    def test_place_black_queen_on_black_place(self):
        board = ChessBoard(size=5)
        black_places = board.black_places
        board.place_black_queen(black_places[0])

        self.assertEqual(board.queens, [BlackQueen(row=0, column=0)])

    def test_place_black_queen_on_white_place_should_raise_exception(self):
        board = ChessBoard(size=5)
        white_place = board.white_places

        with self.assertRaises(BadQueenPlacementException):
            board.place_black_queen(white_place[0])
