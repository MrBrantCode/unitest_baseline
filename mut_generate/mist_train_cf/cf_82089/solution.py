"""
QUESTION:
Write a function `expected_distance(n)` that calculates the aggregate of the expected distance between two points randomly selected within each of the potential hollow square laminae of dimension `n`, rounded to the fourth decimal place. The hollow square lamina is an integer-sized square with a side length of `n >= 3` composed of `n^2` unit squares, from which a rectangle made up of `x * y` unit squares (`1 <= x, y <= n - 2`) has been excised from the original square.
"""

def expected_distance(n):
    grid = [[(i**2 + j**2)**0.5 / 15 + 2 * (i + j) / 15 for j in range(n)] for i in range(n)]

    for i in range(1, n):
        for j in range(1, n):
            grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]

    result = 0
    
    for x in range(n - 1):
        for y in range(n - 1):
            for i in range(x + 2, n):
                for j in range(y + 2, n):
                    result += grid[i][j] - grid[i][y+1] - grid[x+1][j] + grid[x+1][y+1]
    return round(result, 4)