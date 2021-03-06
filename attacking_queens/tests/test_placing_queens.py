import unittest

from attacking_queens.board import ChessBoard, WhiteQueen
from attacking_queens.board import BlackQueen
from attacking_queens.exceptions import BadQueenPlacementException


class PlacingQueensTests(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(size=5)

    def test_place_black_queen_on_black_place(self):
        black_places = self.board.black_places[0]
        self.board.place_black_queen(black_places)
        self.assertEqual(self.board.black_queens(), [BlackQueen(row=0, column=0)])

    def test_place_black_queen_on_white_place_should_raise_exception(self):
        white_place = self.board.white_places[0]
        with self.assertRaises(BadQueenPlacementException):
            self.board.place_black_queen(white_place)

    def test_place_white_queen_on_white_place(self):
        white_places = self.board.white_places[0]
        self.board.place_white_queen(white_places)
        self.assertEqual(self.board.white_queens(), [WhiteQueen(row=0, column=1)])

    def test_place_white_queen_on_black_place_should_raise_exception(self):
        black_place = self.board.black_places[0]
        with self.assertRaises(BadQueenPlacementException):
            self.board.place_white_queen(black_place)

    def test_place_two_black_queens_on_same_place_should_raise_exception(self):
        black_queen = BlackQueen(row=0, column=0)
        self.board.place_black_queen(black_queen)
        with self.assertRaises(BadQueenPlacementException):
            self.board.place_black_queen(black_queen)

    def test_place_two_white_queens_on_same_place_should_raise_exception(self):
        white_queen = WhiteQueen(row=0, column=1)
        self.board.place_white_queen(white_queen)
        with self.assertRaises(BadQueenPlacementException):
            self.board.place_white_queen(white_queen)

    def test_place_two_attacking_queens_opposite_color(self):
        self.fail("Work for tomorrow")
