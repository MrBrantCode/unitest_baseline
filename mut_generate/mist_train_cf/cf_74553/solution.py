"""
QUESTION:
Write a function named `diamond_sum` that takes a diamond-shaped grid of numbers represented as a list of lists as input. The function should return a single numerical value calculated by sorting the numbers in each diagonal line using the merge sort algorithm and then summing up the sorted numbers. The input list of lists is assumed to be a valid diamond shape, where the number of elements in each row increases by one until the middle row and then decreases by one. The function should not use built-in sorting functions.
"""

def diamond_sum(diamond):
    """
    This function calculates the sum of numbers in each diagonal line of a diamond-shaped grid.
    It uses the merge sort algorithm for sorting the numbers in each diagonal line.

    Args:
    diamond (list of lists): A 2D list representing the diamond shape.

    Returns:
    int: The sum of numbers in each diagonal line of the diamond.
    """

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

    def merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left[0] < right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    mid = len(diamond) // 2
    diagonal_lines = [[] for _ in range(len(diamond))]

    for i, row in enumerate(diamond):
        row_len = len(row)
        for j, cell in enumerate(row):
            if i <= mid:
                diagonal = mid - row_len // 2 + j
            else:
                diagonal = mid - row_len // 2 + j + (i - mid)
            diagonal_lines[diagonal].append(cell)

    sorted_diagonal_lines = list(map(merge_sort, diagonal_lines))
    sums = list(map(sum, sorted_diagonal_lines))
    value = sum(sums)

    return value