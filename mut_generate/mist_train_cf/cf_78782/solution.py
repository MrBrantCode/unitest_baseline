"""
QUESTION:
Write a function `max_height(cubes)` that takes a list of 3D cubes as input where each cube is represented as a list of three integers `[length, width, height]`, and returns the maximum number of cubes that can be stacked on top of each other. The function should follow these rules:

* One cube can be stacked on top of another if and only if the length, width, and height of the top cube are all less than those of the bottom cube.
* The function should not consider rotations of the cubes.
* The input list `cubes` will contain between 1 and 5000 cubes, each with dimensions between 1 and 10^4.
"""

def max_height(cubes):
    N = len(cubes)
    cubes = [[0, 0, 0]] + sorted(map(sorted, cubes))
    dp = [0]*(N+1)
    for i in range(1, N+1):
        dp[i] = cubes[i][2]
        for j in range(1, i):
            if cubes[i][0] > cubes[j][0] and cubes[i][1] > cubes[j][1] and cubes[i][2] > cubes[j][2]:
                dp[i] = max(dp[i], dp[j] + cubes[i][2])
    return max(dp)