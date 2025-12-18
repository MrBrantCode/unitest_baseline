"""
QUESTION:
Write a function `leastBricks` that takes a list of rows, where each row is a list of integers representing the width of each stone in the row. The function should return the minimum number of stones that must be crossed by a horizontal line drawn from left to right. The line cannot be drawn along the top or bottom edge of the wall. The width sum of stones in different rows is the same and will not exceed INT_MAX. The number of stones in each row is in range [1,10,000]. The height of the wall is in range [1,10,000]. The total number of stones of the wall will not exceed 20,000.
"""

from collections import defaultdict

def leastBricks(wall):
    crevices = defaultdict(int)
    for row in wall:
        c = 0
        for i in range(len(row)-1):
            c += row[i]
            crevices[c] += 1
    
    return len(wall) - max(crevices.values()) if crevices else len(wall)