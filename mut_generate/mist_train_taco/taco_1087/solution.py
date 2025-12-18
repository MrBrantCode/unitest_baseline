"""
QUESTION:
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:


Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

def solve_n_queens(n: int) -> list[list[str]]:
    def helper(current_index: int, aux: list[list[str]], rows_with_queen: list[int], all_solutions: list[list[list[str]]]):
        for i in range(n):
            if i not in rows_with_queen:
                (x, y) = (current_index - 1, i - 1)
                while x >= 0 and y >= 0 and aux[x][y] != 'Q':
                    x -= 1
                    y -= 1
                if x != -1 and y != -1:
                    continue
                (x, y) = (current_index - 1, i + 1)
                while x >= 0 and y < n and aux[x][y] != 'Q':
                    x -= 1
                    y += 1
                if x != -1 and y != n:
                    continue
                aux[current_index][i] = 'Q'
                rows_with_queen.append(i)
                if current_index == n - 1:
                    solution = [row[:] for row in aux]
                    all_solutions.append(solution)
                else:
                    helper(current_index + 1, aux, rows_with_queen, all_solutions)
                aux[current_index][i] = '.'
                rows_with_queen.pop()

    aux = [['.' for _ in range(n)] for _ in range(n)]
    rows_with_queen = []
    all_solutions = []
    helper(0, aux, rows_with_queen, all_solutions)
    
    result = []
    for sol in all_solutions:
        result.append([''.join(row) for row in sol])
    
    return result