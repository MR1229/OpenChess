from chess.moves import get_pseudo_legal_moves
from chess.constants import WHITE, BLACK


def is_square_attacked(board, row, col, by_color):
    for r in range(8):
        for c in range(8):
            piece = board.get_piece(r, c)
            if piece is not None and piece.color == by_color:
                if (row, col) in get_pseudo_legal_moves(board, r, c):
                    return True
    return False


def is_king_in_check(board, color):
    king_position = board.find_king(color)
    if king_position is None:
        return False

    king_row, king_col = king_position
    opponent_color = BLACK if color == WHITE else WHITE
    return is_square_attacked(board, king_row, king_col, opponent_color)


def get_legal_moves(board, row, col):
    piece = board.get_piece(row, col)
    if piece is None:
        return []

    legal_moves = []
    for target_row, target_col in get_pseudo_legal_moves(board, row, col):
        simulated_board = board.clone()
        simulated_board.move_piece(row, col, target_row, target_col)
        if not is_king_in_check(simulated_board, piece.color):
            legal_moves.append((target_row, target_col))

    return legal_moves
