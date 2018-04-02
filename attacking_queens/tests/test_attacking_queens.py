import unittest

from attacking_queens.board import ChessBoard


class ChessBoardTests(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(size=5)

    def test_chess_board_size(self):
        self.assertEqual(self.board.size, 5)

    def test_chess_board_available_black_places(self):
        self.assertEqual(self.board.black_size, 13)

    def test_chess_board_available_white_places(self):
        self.assertEqual(self.board.white_size, 12)
