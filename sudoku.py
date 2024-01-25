SUDOKU_SIZE = 9


def checkPhistomephelRing(sudokuMatrix):
    squares = [
        sudokuMatrix[0][0],
        sudokuMatrix[0][1],
        sudokuMatrix[1][0],
        sudokuMatrix[1][1],
        sudokuMatrix[0][SUDOKU_SIZE - 2],
        sudokuMatrix[0][SUDOKU_SIZE - 1],
        sudokuMatrix[1][SUDOKU_SIZE - 2],
        sudokuMatrix[1][SUDOKU_SIZE - 1],
        sudokuMatrix[SUDOKU_SIZE - 2][0],
        sudokuMatrix[SUDOKU_SIZE - 2][1],
        sudokuMatrix[SUDOKU_SIZE - 1][0],
        sudokuMatrix[SUDOKU_SIZE - 1][1],
        sudokuMatrix[SUDOKU_SIZE - 2][SUDOKU_SIZE - 2],
        sudokuMatrix[SUDOKU_SIZE - 2][SUDOKU_SIZE - 1],
        sudokuMatrix[SUDOKU_SIZE - 1][SUDOKU_SIZE - 2],
        sudokuMatrix[SUDOKU_SIZE - 1][SUDOKU_SIZE - 1],
    ]
    ring = (
        sudokuMatrix[2][2:7]
        + [
            sudokuMatrix[3][2],
            sudokuMatrix[4][2],
            sudokuMatrix[5][2],
            sudokuMatrix[3][6],
            sudokuMatrix[4][6],
            sudokuMatrix[5][6],
        ]
        + sudokuMatrix[6][2:7]
    )
    squares.sort()
    ring.sort()
    return squares == ring
