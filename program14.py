# 14. Implement solveNQueens(n: int) -> List[List[str]] function taking board dimension and
# returning all valid board layout configurations.

from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    result = []

    board = [["."] * n for _ in range(n)]

    # Sets to keep track of occupied columns and diagonals
    columns = set()
    positive_diagonals = set()  # row + col
    negative_diagonals = set()  # row - col

    def backtrack(row):
        # All queens have been placed
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):

            # Check whether this position is safe
            if col in columns:
                continue

            if row + col in positive_diagonals:
                continue

            if row - col in negative_diagonals:
                continue

            # Place queen
            board[row][col] = "Q"
            columns.add(col)
            positive_diagonals.add(row + col)
            negative_diagonals.add(row - col)

            # Move to next row
            backtrack(row + 1)

            # Backtrack: remove queen
            board[row][col] = "."
            columns.remove(col)
            positive_diagonals.remove(row + col)
            negative_diagonals.remove(row - col)

    backtrack(0)

    return result


# Example
n = 4

solutions = solveNQueens(n)

print("Number of solutions:", len(solutions))

for solution in solutions:
    print()
    for row in solution:
        print(row)