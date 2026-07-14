const gameState = {
    board: [],
    currentTurn: "white",
    moveHistory: [],
    check: false,
    selectedSquare: null,
    legalMoves: [],
};

async function fetchState() {
    const response = await fetch("/api/state");
    const data = await response.json();
    applyState(data);
}

async function fetchLegalMoves(row, col) {
    const response = await fetch("/api/legal-moves", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ row, col }),
    });
    const data = await response.json();
    return data.legal_moves || [];
}

async function submitMove(fromRow, fromCol, toRow, toCol) {
    const response = await fetch("/api/move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            from_row: fromRow,
            from_col: fromCol,
            to_row: toRow,
            to_col: toCol,
        }),
    });
    return response.json();
}

async function resetGame() {
    await fetch("/api/reset", { method: "POST" });
    gameState.selectedSquare = null;
    gameState.legalMoves = [];
    await fetchState();
}

function applyState(data) {
    gameState.board = data.board;
    gameState.currentTurn = data.current_turn;
    gameState.moveHistory = data.move_history;
    gameState.check = data.check;
    draw();
    updateStatusPanel(gameState);
}

function draw() {
    renderBoard(gameState.board, {
        selectedSquare: gameState.selectedSquare,
        legalMoves: gameState.legalMoves,
        kingInCheckSquare: gameState.check ? findKingSquare(gameState.board, gameState.currentTurn) : null,
        onSquareClick: handleSquareClick,
    });
}

function findKingSquare(board, color) {
    for (let row = 0; row < 8; row += 1) {
        for (let col = 0; col < 8; col += 1) {
            const piece = board[row][col];
            if (piece && piece.color === color && piece.type === "king") {
                return { row, col };
            }
        }
    }
    return null;
}

async function handleSquareClick(row, col) {
    const clickedPiece = gameState.board[row][col];

    if (gameState.selectedSquare) {
        const isLegalTarget = gameState.legalMoves.some((move) => move[0] === row && move[1] === col);

        if (isLegalTarget) {
            const result = await submitMove(
                gameState.selectedSquare.row,
                gameState.selectedSquare.col,
                row,
                col
            );
            gameState.selectedSquare = null;
            gameState.legalMoves = [];
            if (result.success) {
                await fetchState();
            } else {
                draw();
            }
            return;
        }

        if (clickedPiece && clickedPiece.color === gameState.currentTurn) {
            await selectSquare(row, col);
            return;
        }

        gameState.selectedSquare = null;
        gameState.legalMoves = [];
        draw();
        return;
    }

    if (clickedPiece && clickedPiece.color === gameState.currentTurn) {
        await selectSquare(row, col);
    }
}

async function selectSquare(row, col) {
    gameState.selectedSquare = { row, col };
    gameState.legalMoves = await fetchLegalMoves(row, col);
    draw();
}

document.addEventListener("DOMContentLoaded", () => {
    fetchState();
    document.getElementById("reset-button").addEventListener("click", resetGame);
});
