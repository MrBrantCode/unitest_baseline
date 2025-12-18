"""
QUESTION:
Write a function named `spiral_traversal` that calculates the sum of all elements in a given 2D list (matrix) by traversing it in a spiral order, starting from the top-left corner and moving clockwise. The function should take a 2D list as input and return the calculated sum.
"""

def spiral_traversal(matrix):
    """
    This function takes a 2D list called `matrix` as input and returns the sum of all elements
    traversing the matrix in a spiral order starting from the top-left corner and moving clockwise.
    """
    def spiral_coords(r1, c1, r2, c2):
        """
        This helper function generates the coordinates for the elements of the matrix as tuples.
        """
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    if not matrix:
        return 0
    ans = 0
    r1, r2 = 0, len(matrix) - 1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in spiral_coords(r1, c1, r2, c2):
            ans += matrix[r][c]
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans