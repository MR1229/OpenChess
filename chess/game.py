from chess.board import Board
from chess.rules import get_legal_moves, is_king_in_check
from chess.constants import WHITE, BLACK


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = WHITE
        self.move_history = []

    def get_legal_moves_for_square(self, row, col):
        piece = self.board.get_piece(row, col)
        if piece is None or piece.color != self.current_turn:
            return []
        return get_legal_moves(self.board, row, col)

    def make_move(self, from_row, from_col, to_row, to_col):
        piece = self.board.get_piece(from_row, from_col)
        if piece is None or piece.color != self.current_turn:
            return {"success": False, "error": "No piece of the current player on that square"}

        legal_moves = get_legal_moves(self.board, from_row, from_col)
        if (to_row, to_col) not in legal_moves:
            return {"success": False, "error": "That move is not legal"}

        captured_piece = self.board.move_piece(from_row, from_col, to_row, to_col)

        self.move_history.append({
            "piece": piece.piece_type,
            "color": piece.color,
            "from": [from_row, from_col],
            "to": [to_row, to_col],
            "captured": captured_piece.piece_type if captured_piece else None,
        })

        self.current_turn = BLACK if self.current_turn == WHITE else WHITE

        return {
            "success": True,
            "captured": captured_piece.piece_type if captured_piece else None,
            "current_turn": self.current_turn,
            "check": is_king_in_check(self.board, self.current_turn),
        }

    def get_state(self):
        return {
            "board": self.board.to_dict(),
            "current_turn": self.current_turn,
            "move_history": self.move_history,
            "check": is_king_in_check(self.board, self.current_turn),
        }

    def reset(self):
        self.__init__()
