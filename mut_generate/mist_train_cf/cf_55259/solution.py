"""
QUESTION:
The function `prisonAfterNDays` takes in two parameters: `cells` (an array of 8 integers representing the initial state of the prison) and `N` (an integer representing the number of days). The function should return the state of the prison after `N` days, where each cell's state is determined by the rules: if a cell's two adjacent neighbors are both occupied or both vacant, the cell becomes occupied; otherwise, it becomes vacant. The first and last cells have only one neighbor. The function should handle the case where `N` is large by exploiting the cyclical nature of the prison's state changes. Constraints: `len(cells) == 8`, `cells[i]` is either 0 or 1, and `1 <= N <= 10^9`.
"""

def prisonAfterNDays(cells, N):
    def nextDay(cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]

    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            N %= seen[c] - N
        seen[c] = N

        if N >= 1:
            N -= 1
            cells = nextDay(cells)

    return cells