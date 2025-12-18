"""
QUESTION:
Create a function named `find_perfect_cubes` that takes a positive integer `n` as input and returns a list of all perfect cubes between 1 and `n` (inclusive).
"""

def find_perfect_cubes(n):
    cubes = []
    for i in range(1, n+1):
        cube = i ** 3
        if cube <= n:
            cubes.append(cube)
        else:
            break
    return cubes