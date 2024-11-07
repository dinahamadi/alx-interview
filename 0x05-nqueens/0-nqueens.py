#!/usr/bin/python3
"""
a python script that a program that solves the N queens problem
"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """Use backtracking to solve the N queens problem."""
    if col == len(board):
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[row][col] = 0


def print_solutions(n):
    """Initialize board and solve the N queens problem."""
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)


def main():
    """Main function to parse arguments and execute the N queens solution."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    print_solutions(n)


if __name__ == "__main__":
    main()
