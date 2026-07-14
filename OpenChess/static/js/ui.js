function updateStatusPanel(state) {
    const turnIndicator = document.getElementById("turn-indicator");
    const checkIndicator = document.getElementById("check-indicator");
    const historyList = document.getElementById("move-history");

    const turnLabel = state.currentTurn === "white" ? "White to move" : "Black to move";
    turnIndicator.textContent = turnLabel;
    turnIndicator.classList.toggle("turn-indicator--black", state.currentTurn === "black");

    checkIndicator.hidden = !state.check;

    historyList.innerHTML = "";
    state.moveHistory.forEach((move, index) => {
        const entry = document.createElement("li");
        entry.textContent = formatMoveEntry(move, index);
        historyList.appendChild(entry);
    });
    historyList.scrollTop = historyList.scrollHeight;
}

function formatMoveEntry(move, index) {
    const files = ["a", "b", "c", "d", "e", "f", "g", "h"];
    const fromSquare = `${files[move.from[1]]}${8 - move.from[0]}`;
    const toSquare = `${files[move.to[1]]}${8 - move.to[0]}`;
    const captureNote = move.captured ? ` x${move.captured}` : "";
    const moveNumber = Math.floor(index / 2) + 1;
    const prefix = index % 2 === 0 ? `${moveNumber}.` : `${moveNumber}...`;
    return `${prefix} ${move.piece} ${fromSquare}-${toSquare}${captureNote}`;
}
