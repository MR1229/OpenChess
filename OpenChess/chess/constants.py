BOARD_SIZE = 8

WHITE = "white"
BLACK = "black"

PAWN = "pawn"
KNIGHT = "knight"
BISHOP = "bishop"
ROOK = "rook"
QUEEN = "queen"
KING = "king"

BACK_RANK_ORDER = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]

PIECE_SYMBOLS = {
    (WHITE, PAWN): "\u2659",
    (WHITE, KNIGHT): "\u2658",
    (WHITE, BISHOP): "\u2657",
    (WHITE, ROOK): "\u2656",
    (WHITE, QUEEN): "\u2655",
    (WHITE, KING): "\u2654",
    (BLACK, PAWN): "\u265F",
    (BLACK, KNIGHT): "\u265E",
    (BLACK, BISHOP): "\u265D",
    (BLACK, ROOK): "\u265C",
    (BLACK, QUEEN): "\u265B",
    (BLACK, KING): "\u265A",
}
