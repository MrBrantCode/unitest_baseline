"""
QUESTION:
Design a function named `count_divisible_cubes` that takes two integers `lower` and `upper` as input. The function should calculate the cube of each integer within the range from `lower` to `upper` (inclusive of `lower`, exclusive of `upper`) and return a dictionary containing two counts: the total number of cubes and the number of cubes that are divisible by 6.
"""

def count_divisible_cubes(lower, upper):
    cube_counts = {"total": 0, "divisible_by_6": 0}
    for i in range(lower, upper):
        cube = i ** 3
        cube_counts["total"] += 1
        if cube % 6 == 0:
            cube_counts["divisible_by_6"] += 1
    return cube_counts