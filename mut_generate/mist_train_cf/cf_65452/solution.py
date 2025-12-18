"""
QUESTION:
Write a function `minTimeToEmptyWells(grid, bucket_capacity)` that calculates the minimum number of hours needed to empty all wells, given a grid of wells where each row represents a well and each '1' denotes a unit of water, and the bucket capacity. Each well can be emptied only once per hour.
"""

def minTimeToEmptyWells(grid, bucket_capacity):
    count = [0] * len(grid[0])
    for row in grid:
        for j in range(len(row)):
            count[j] += row[j]
    count.sort()

    time = 0
    while count:
        i = len(count) - 1
        while i >= 0 and count[i] > 0:
            count[i] -= bucket_capacity
            i -= 1
        count = [x for x in count if x > 0]
        time += 1

    return time - 1 if len(grid[0]) > bucket_capacity else time