#!/usr/bin/python3
"""Solve the N queens puzzle and print every solution."""
import sys


def is_safe(queens, row, col):
    """Return True if a queen at (row, col) is not attacked."""
    for r, c in queens:
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


def solve(n, row, queens, solutions):
    """Place queens row by row using backtracking."""
    if row == n:
        solutions.append([q[:] for q in queens])
        return
    for col in range(n):
        if is_safe(queens, row, col):
            queens.append([row, col])
            solve(n, row + 1, queens, solutions)
            queens.pop()


def main():
    """Check the arguments, solve the puzzle and print the solutions."""
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

    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
