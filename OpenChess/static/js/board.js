const PIECE_SYMBOLS = {
    white: { pawn: "\u2659", knight: "\u2658", bishop: "\u2657", rook: "\u2656", queen: "\u2655", king: "\u2654" },
    black: { pawn: "\u265F", knight: "\u265E", bishop: "\u265D", rook: "\u265C", queen: "\u265B", king: "\u265A" },
};

const FILE_LABELS = ["a", "b", "c", "d", "e", "f", "g", "h"];

function renderBoard(boardState, options) {
    const { selectedSquare, legalMoves, kingInCheckSquare, onSquareClick } = options;
    const boardElement = document.getElementById("board");
    boardElement.innerHTML = "";

    for (let row = 0; row < 8; row += 1) {
        for (let col = 0; col < 8; col += 1) {
            const square = document.createElement("div");
            const isLight = (row + col) % 2 === 0;
            square.className = `square ${isLight ? "square--light" : "square--dark"}`;
            square.dataset.row = String(row);
            square.dataset.col = String(col);

            if (selectedSquare && selectedSquare.row === row && selectedSquare.col === col) {
                square.classList.add("square--selected");
            }

            if (kingInCheckSquare && kingInCheckSquare.row === row && kingInCheckSquare.col === col) {
                square.classList.add("square--check");
            }

            const isLegalTarget = legalMoves.some((move) => move[0] === row && move[1] === col);
            if (isLegalTarget) {
                const isCapture = boardState[row][col] !== null;
                square.classList.add(isCapture ? "square--legal-capture" : "square--legal-move");
            }

            const piece = boardState[row][col];
            if (piece) {
                const pieceElement = document.createElement("span");
                pieceElement.className = `piece piece--${piece.color}`;
                pieceElement.textContent = PIECE_SYMBOLS[piece.color][piece.type];
                square.appendChild(pieceElement);
            }

            if (col === 0) {
                const rankLabel = document.createElement("span");
                rankLabel.className = "coordinate-label coordinate-label--rank";
                rankLabel.textContent = String(8 - row);
                square.appendChild(rankLabel);
            }

            if (row === 7) {
                const fileLabel = document.createElement("span");
                fileLabel.className = "coordinate-label coordinate-label--file";
                fileLabel.textContent = FILE_LABELS[col];
                square.appendChild(fileLabel);
            }

            square.addEventListener("click", () => onSquareClick(row, col));
            boardElement.appendChild(square);
        }
    }
}
