# OpenChess

An original, modern chess web application inspired by Chess.com. Built in
phases, starting from a pure Python chess engine with a minimal Flask
frontend.

## Phase 1

- Pure Python chess engine: legal move generation for every piece, capturing,
  turn management, and check detection.
- Flask backend exposing a small JSON API for game state, legal moves, and
  making moves.
- Minimal, responsive HTML/CSS/JS frontend rendered with Flask templates.
- No database, no authentication, no AI yet — a single in-memory game
  session.

Not yet implemented (future phases): castling, en passant, promotion,
checkmate/stalemate detection, draw offers, resignation, undo, timers, and
AI opponents.

## Project Structure

```
OpenChess/
    app.py
    requirements.txt
    README.md
    .gitignore
    chess/
        board.py
        piece.py
        moves.py
        rules.py
        game.py
        constants.py
    routes/
        home.py
        api.py
    templates/
        index.html
    static/
        css/
            style.css
            board.css
        js/
            board.js
            game.js
            ui.js
        images/
            pieces/
        sounds/
    tests/
```

## Setup

Requires Python 3.10+.

```bash
cd OpenChess
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## API

| Method | Endpoint            | Description                              |
|--------|----------------------|-------------------------------------------|
| GET    | `/api/state`          | Current board, turn, move history, check |
| POST   | `/api/legal-moves`    | `{ "row": int, "col": int }` -> legal moves for that square |
| POST   | `/api/move`           | `{ "from_row", "from_col", "to_row", "to_col" }` -> attempt a move |
| POST   | `/api/reset`          | Reset to a fresh starting position       |

## How to Play

Click a piece belonging to the side whose turn it is. Legal destination
squares are highlighted. Click a highlighted square to move, click another
one of your own pieces to change your selection, or click an empty
non-legal square to deselect.
