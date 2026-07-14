from chess.constants import WHITE, PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING

KNIGHT_OFFSETS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
DIAGONAL_DIRECTIONS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
STRAIGHT_DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ALL_DIRECTIONS = DIAGONAL_DIRECTIONS + STRAIGHT_DIRECTIONS


def get_pseudo_legal_moves(board, row, col):
    piece = board.get_piece(row, col)
    if piece is None:
        return []

    if piece.piece_type == PAWN:
        return _pawn_moves(board, row, col, piece)
    if piece.piece_type == KNIGHT:
        return _knight_moves(board, row, col, piece)
    if piece.piece_type == BISHOP:
        return _sliding_moves(board, row, col, piece, DIAGONAL_DIRECTIONS)
    if piece.piece_type == ROOK:
        return _sliding_moves(board, row, col, piece, STRAIGHT_DIRECTIONS)
    if piece.piece_type == QUEEN:
        return _sliding_moves(board, row, col, piece, ALL_DIRECTIONS)
    if piece.piece_type == KING:
        return _king_moves(board, row, col, piece)
    return []


def _pawn_moves(board, row, col, piece):
    moves = []
    direction = -1 if piece.color == WHITE else 1
    start_row = 6 if piece.color == WHITE else 1

    one_step_row = row + direction
    if board.is_on_board(one_step_row, col) and board.get_piece(one_step_row, col) is None:
        moves.append((one_step_row, col))
        two_step_row = row + direction * 2
        if row == start_row and board.get_piece(two_step_row, col) is None:
            moves.append((two_step_row, col))

    for delta_col in (-1, 1):
        target_row = row + direction
        target_col = col + delta_col
        if board.is_on_board(target_row, target_col):
            target_piece = board.get_piece(target_row, target_col)
            if target_piece is not None and target_piece.color != piece.color:
                moves.append((target_row, target_col))

    return moves


def _knight_moves(board, row, col, piece):
    moves = []
    for delta_row, delta_col in KNIGHT_OFFSETS:
        target_row, target_col = row + delta_row, col + delta_col
        if board.is_on_board(target_row, target_col):
            target_piece = board.get_piece(target_row, target_col)
            if target_piece is None or target_piece.color != piece.color:
                moves.append((target_row, target_col))
    return moves


def _sliding_moves(board, row, col, piece, directions):
    moves = []
    for delta_row, delta_col in directions:
        target_row, target_col = row + delta_row, col + delta_col
        while board.is_on_board(target_row, target_col):
            target_piece = board.get_piece(target_row, target_col)
            if target_piece is None:
                moves.append((target_row, target_col))
            else:
                if target_piece.color != piece.color:
                    moves.append((target_row, target_col))
                break
            target_row += delta_row
            target_col += delta_col
    return moves


def _king_moves(board, row, col, piece):
    moves = []
    for delta_row in (-1, 0, 1):
        for delta_col in (-1, 0, 1):
            if delta_row == 0 and delta_col == 0:
                continue
            target_row, target_col = row + delta_row, col + delta_col
            if board.is_on_board(target_row, target_col):
                target_piece = board.get_piece(target_row, target_col)
                if target_piece is None or target_piece.color != piece.color:
                    moves.append((target_row, target_col))
    return moves
