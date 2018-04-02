import unittest

from attacking_queens.board import BoardSize
from attacking_queens.board import ChessBoard


class ChessBoardTests(unittest.TestCase):

    def setUp(self):
        self.board = ChessBoard(size=5)

    def test_chess_board_size(self):
        self.assertEqual(self.board.size, 5)

    def test_available_places_for_even_size_board(self):
        even_sized_board = ChessBoard(size=8)
        self.assertEqual(even_sized_board.board_size, BoardSize(black_size=32, white_size=32))

    def test_available_places_for_odd_size_board(self):
        odd_sized_board = ChessBoard(size=5)
        self.assertEqual(odd_sized_board.board_size, BoardSize(black_size=13, white_size=12))

    def test_board_of_size_one_should_have_one_black_and_zero_white_places(self):
        board = ChessBoard(size=1)
        self.assertEqual(board.black_places, [(0, 0)])
        self.assertEqual(board.white_places, [])

    def test_board_of_size_two_should_have_two_black_and_two_white_places(self):
        board = ChessBoard(size=2)
        self.assertEqual(board.black_places, [(0, 0), (1, 1)])
        self.assertEqual(board.white_places, [(0, 1), (1, 0)])

    def test_should_get_all_available_black_places(self):
        expected_black_places = [
            (0, 0),         (0, 2),         (0, 4),
                    (1, 1),          (1, 3),
            (2, 0),         (2, 2),         (2, 4),
                    (3, 1),          (3, 3),
            (4, 0),         (4, 2),         (4, 4)
        ]
        expected_white_places = [
                    (0, 1),         (0, 3),
            (1, 0),         (1, 2),         (1, 4),
                    (2, 1),         (2, 3),
            (3, 0),         (3, 2),         (3, 4),
                    (4, 1),         (4, 3)
        ]
        self.assertEqual(self.board.black_places, expected_black_places)
        self.assertEqual(self.board.white_places, expected_white_places)
