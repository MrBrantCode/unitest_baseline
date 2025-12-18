"""
QUESTION:
Write a function `find_median(grid)` that takes a 2D grid of sorted integers as input, where each inner list represents a row and integers in each row are sorted in ascending order, but not necessarily relative to other rows. The function should return the median of all integers in the grid. If the total number of integers is even, return the average of the two middle elements.
"""

def find_median(grid):
    flat_list = [num for row in grid for num in row]
    flat_list.sort()
    length = len(flat_list)
    if length % 2 == 0:
        return (flat_list[length // 2 - 1] + flat_list[length // 2]) / 2
    else:
        return flat_list[length // 2]