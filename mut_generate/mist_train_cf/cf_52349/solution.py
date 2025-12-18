"""
QUESTION:
Write a function `fallingSquares(positions)` that takes a list of cube positions `positions` where each cube position is a list `[left, bottom, side_length]`. The function should return a list `ans` where `ans[i]` is the maximum height of any cube after releasing the first `i + 1` cubes.

Each cube has a left-most point at `positions[i][0]`, a bottom-most point at `positions[i][1]`, and a side length of `positions[i][2]`. Cubes are infinitely sticky on their bottom face and will remain fixed to any positive area surface they touch.

The input list `positions` has a length between 1 and 1000 (inclusive), and each cube position has the following constraints: `1 <= positions[i][0] <= 10^8`, `1 <= positions[i][1] <= 10^8`, and `1 <= positions[i][2] <= 10^6`.
"""

def fallingSquares(positions):
    ans = [0] 
    intervals = [] 

    for left, bot, size in positions:
        right, up = left + size, bot + size

        # calculate the maximum height of shadows that overlaps with this square
        h = max([h for i, h in intervals if i[0] < right and left < i[1]] or [0])

        # add to height list
        ans.append(max(ans[-1], h + size))

        # update intervals
        intervals.append(((left, right), h + size))

    return ans[1:]