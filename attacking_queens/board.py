from typing import NamedTuple, List, Tuple

BoardSize = NamedTuple('BoardSize', [('black_size', int), ('white_size', int)])

PlaceList = List[Tuple[int, int]]


class ChessBoard:
    def __init__(self, size: int) -> None:
        self._white_places = []
        self._black_places = []
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
