"""
QUESTION:
Write a function `maxStackedCubes` that takes a 3D array of integers `cubes` and an integer `W` as input, where `cubes[i] = [length, width, height, weight]` represents a cube, and returns the maximum number of cubes that can be stacked on top of each other without exceeding the weight limit `W`. One cube can be stacked on top of another if and only if the length, width, and height of the top cube are all less than those of the bottom cube. The function should not consider rotating the cubes.
"""

def maxStackedCubes(cubes, W):
    # sort cubes by volume and weight
    cubes = sorted(cubes, key=lambda x: (-x[0]*x[1]*x[2], x[3]))

    dp = [0] * (W + 1)
    for l, w, h, wt in cubes:
        for j in range(W, wt - 1, -1):
            dp[j] = max(dp[j], dp[j - wt] + 1)

    return dp[-1]