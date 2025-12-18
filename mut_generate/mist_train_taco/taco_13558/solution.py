"""
QUESTION:
You are given n points on a line with their coordinates x_{i}. Find the point x so the sum of distances to the given points is minimal.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 3·10^5) — the number of points on the line.

The second line contains n integers x_{i} ( - 10^9 ≤ x_{i} ≤ 10^9) — the coordinates of the given n points.


-----Output-----

Print the only integer x — the position of the optimal point on the line. If there are several optimal points print the position of the leftmost one. It is guaranteed that the answer is always the integer.


-----Example-----
Input
4
1 2 3 4

Output
2
"""

def find_optimal_point(n: int, coordinates: list) -> int:
    """
    Finds the optimal point on a line such that the sum of distances to the given points is minimal.

    Parameters:
    n (int): The number of points on the line.
    coordinates (list): A list of integers representing the coordinates of the points.

    Returns:
    int: The position of the optimal point on the line. If there are several optimal points, returns the position of the leftmost one.
    """
    coordinates.sort()
    if n % 2 == 0:
        return coordinates[int(n / 2) - 1]
    else:
        return coordinates[int(n / 2)]