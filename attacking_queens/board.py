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
        return [(0, 0)]

    @property
    def white_places(self):
        return []
