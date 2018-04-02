class ChessBoard:
    def __init__(self, size: int):
        self.size = size

    @property
    def white_size(self):
        return int(self.size ** 2 / 2)

    @property
    def black_size(self):
        return self.size ** 2 - self.white_size

    @property
    def black_places(self):
        if self.size == 1:
            return [(0, 0)]
        black_places = []
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:
                    black_places.append((i, j,))
        return black_places

    @property
    def white_places(self):
        if self.size == 1:
            return []
        white_places = []
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 != 0:
                    white_places.append((i, j,))
        return white_places
