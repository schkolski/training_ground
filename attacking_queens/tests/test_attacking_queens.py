import unittest

from attacking_queens.board import ChessBoard


class ChessBoardTests(unittest.TestCase):

    def test_chess_board(self):
        board = ChessBoard(size=5)

        self.assertEqual(board.size, 5)
