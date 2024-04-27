#!/usr/bin/python3
"""import modules"""
import sys


def print_error_message(message):
    """error message"""
    print(message)
    sys.exit(1)


def is_valid_position(board, row, col):
    """is valid position"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, results):
    """solve nqueens"""
    if col >= len(board):
        results.append([(i, board[i].index(1)) for i in range(len(board))])
        return
    for i in range(len(board)):
        if is_valid_position(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, results)
            board[i][col] = 0  # backtrack


def nqueens(n):
    """nqueens"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    solve_nqueens(board, 0, results)
    return results


if __name__ == "__main__":
    """entry point"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_error_message("N must be a number")

    if n < 4:
        print_error_message("N must be at least 4")

    solutions = nqueens(n)
    for solution in solutions:
        print(solution)
