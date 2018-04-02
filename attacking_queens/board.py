class ChessBoard:
    def __init__(self, size: int):
        self.size = size
        self.black_size = int(size * size / 2) + 1
