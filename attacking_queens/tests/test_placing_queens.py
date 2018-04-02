import unittest

from attacking_queens.board import ChessBoard
from attacking_queens.board import BlackQueen
from attacking_queens.exceptions import BadQueenPlacementException


class PlacingQueensTests(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(size=5)

    def test_place_black_queen_on_black_place(self):
        black_places = self.board.black_places
        self.board.place_black_queen(black_places[0])
        self.assertEqual(self.board.queens, [BlackQueen(row=0, column=0)])

    def test_place_black_queen_on_white_place_should_raise_exception(self):
        white_place = self.board.white_places
        with self.assertRaises(BadQueenPlacementException):
            self.board.place_black_queen(white_place[0])
