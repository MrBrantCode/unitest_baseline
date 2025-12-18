"""
QUESTION:
Design a function named `solve_n_queens` that takes an integer `N` as input and returns all possible configurations of placing `N` queens on an `N×N` chessboard such that no two queens threaten each other, with the constraint that no two queens are in the same row or column.
"""

def solve_n_queens(N):
    def can_place(pos, ocuppied_rows):
        for i in range(len(ocuppied_rows)):
            if ocuppied_rows[i] == pos or \
                ocuppied_rows[i] - i == pos - len(ocuppied_rows) or \
                ocuppied_rows[i] + i == pos + len(ocuppied_rows):
                return False
        return True

    def place_queen(n, ocuppied_rows, results):
        if n == N:
            result = []
            for i in ocuppied_rows:
                row = ['.' for _ in range(N)]
                row[i] = 'Q'
                result.append(''.join(row))
            results.append(result)
            return
        for i in range(N):
            if can_place(i, ocuppied_rows):
                ocuppied_rows.append(i)
                place_queen(n + 1, ocuppied_rows, results)
                ocuppied_rows.pop()

    results = []
    place_queen(0, [], results)
    return results