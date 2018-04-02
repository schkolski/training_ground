class ChessBoard:
    def __init__(self, size: int):
        self.size = size

    @property
    def white_size(self):
        return int(self.size ** 2 / 2)

    @property
    def black_size(self):
        return self.size ** 2 - self.white_size
