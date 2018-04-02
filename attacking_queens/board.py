class ChessBoard:
    def __init__(self, size: int):
        self._white_places = []
        self._black_places = []
        self.size = size
        self.initialize_places()

    def initialize_places(self):
        for i in range(self.size):
            for j in range(self.size):
                place_coordinates = (i, j,)
                if (i + j) % 2 == 0:
                    self._black_places.append(place_coordinates)
                else:
                    self._white_places.append(place_coordinates)

    @property
    def white_size(self):
        return int(self.size ** 2 / 2)

    @property
    def black_size(self):
        return self.size ** 2 - self.white_size

    @property
    def black_places(self):
        return self._black_places

    @property
    def white_places(self):
        return self._white_places
