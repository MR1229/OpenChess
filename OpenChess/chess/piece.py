class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.has_moved = False

    def opponent_color(self):
        from chess.constants import WHITE, BLACK
        return BLACK if self.color == WHITE else WHITE

    def __repr__(self):
        return f"{self.color}_{self.piece_type}"
