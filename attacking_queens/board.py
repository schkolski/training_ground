from collections import defaultdict
from typing import NamedTuple, List, Tuple

from attacking_queens.exceptions import BadQueenPlacementException

BoardSize = NamedTuple('BoardSize', [('black_size', int), ('white_size', int)])
PlaceList = List[Tuple[int, int]]
Queen = NamedTuple('BlackQueen', [('row', int), ('column', int)])
BlackQueen = Queen
WhiteQueen = Queen


def validate_queen(queen: Queen, valid_places: PlaceList) -> Queen:
    if queen not in valid_places:
        raise BadQueenPlacementException()
    return queen


class ChessBoard:
    def __init__(self, size: int) -> None:
        self._queens = defaultdict(list)
        self._white_places = list()
        self._black_places = list()
        self.size = size
        self.initialize_available_places()

    def initialize_available_places(self):
        for i in range(self.size):
            for j in range(self.size):
                place_coordinates = (i, j,)
                if (i + j) % 2 == 0:
                    self._black_places.append(place_coordinates)
                else:
                    self._white_places.append(place_coordinates)

    @property
    def board_size(self) -> BoardSize:
        return BoardSize(
            black_size=self.black_size(),
            white_size=self.white_size()
        )

    @property
    def black_places(self) -> PlaceList:
        return self._black_places

    @property
    def white_places(self) -> PlaceList:
        return self._white_places

    def white_size(self) -> int:
        return int(self.size ** 2 / 2)

    def black_size(self) -> int:
        return self.size ** 2 - self.white_size()

    def place_black_queen(self, queen: BlackQueen) -> None:
        valid_queen = validate_queen(queen, self.black_places)
        self._queens['black'].append(valid_queen)

    def place_white_queen(self, queen: WhiteQueen) -> None:
        valid_queen = validate_queen(queen, self.white_places)
        self._queens['white'].append(valid_queen)

    def black_queens(self) -> List[BlackQueen]:
        return self._queens['black']

    def white_queens(self) -> List[WhiteQueen]:
        return self._queens['white']
