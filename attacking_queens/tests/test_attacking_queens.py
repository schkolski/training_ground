import unittest

from attacking_queens.board import ChessBoard


class ChessBoardTests(unittest.TestCase):

    def test_chess_board_size(self):
        board = ChessBoard(size=5)

        self.assertEqual(board.size, 5)

    def test_chess_board_available_black_places(self):
        board = ChessBoard(size=5)

        self.assertEqual(board.black_size, int(5 * 5 / 2) + 1)
