from flask import Blueprint, jsonify, request

api_bp = Blueprint("api", __name__)

_game = None


def set_game(game):
    global _game
    _game = game


@api_bp.route("/state", methods=["GET"])
def get_state():
    return jsonify(_game.get_state())


@api_bp.route("/legal-moves", methods=["POST"])
def legal_moves():
    data = request.get_json(silent=True) or {}
    row = data.get("row")
    col = data.get("col")

    if row is None or col is None:
        return jsonify({"error": "Missing row or col"}), 400

    moves = _game.get_legal_moves_for_square(row, col)
    return jsonify({"legal_moves": moves})


@api_bp.route("/move", methods=["POST"])
def make_move():
    data = request.get_json(silent=True) or {}
    from_row = data.get("from_row")
    from_col = data.get("from_col")
    to_row = data.get("to_row")
    to_col = data.get("to_col")

    if None in (from_row, from_col, to_row, to_col):
        return jsonify({"error": "Missing move coordinates"}), 400

    result = _game.make_move(from_row, from_col, to_row, to_col)
    return jsonify(result)


@api_bp.route("/reset", methods=["POST"])
def reset_game():
    _game.reset()
    return jsonify({"success": True})
