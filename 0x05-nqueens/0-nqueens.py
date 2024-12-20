#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    for r, c in board:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens(N, row + 1, board, solutions)
            board.pop()


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens(N, 0, [], solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
