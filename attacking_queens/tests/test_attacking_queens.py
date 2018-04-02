import unittest

from attacking_queens.board import ChessBoard


class ChessBoardTests(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(size=5)

    def test_chess_board_size(self):
        self.assertEqual(self.board.size, 5)

    def test_available_places_for_even_size_board(self):
        even_sized_board = ChessBoard(size=8)
        self.assertEqual(even_sized_board.black_size, 32)
        self.assertEqual(even_sized_board.white_size, 32)

    def test_available_places_for_odd_size_board(self):
        odd_sized_board = ChessBoard(size=5)
        self.assertEqual(odd_sized_board.black_size, 13)
        self.assertEqual(odd_sized_board.white_size, 12)
