"""
QUESTION:
Implement the `max_triangles(sticks)` function where `sticks` is a list of integers representing the lengths of sticks. The list must have a length between 3 and 1000 (inclusive) and each stick length must be between 1 and 10^6 (inclusive). Return the maximum number of non-degenerate triangles that can be formed using these sticks, where a non-degenerate triangle is a triangle with positive area.
"""

def max_triangles(sticks):
    """
    Returns the maximum number of non-degenerate triangles that can be formed using the given sticks.

    :param sticks: A list of integers representing the lengths of sticks.
    :return: The maximum number of non-degenerate triangles.
    """
    sticks.sort()
    count = 0
    n = len(sticks)
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n):
            while k < n and sticks[i] + sticks[j] > sticks[k]:
                k += 1
            count += k - j - 1
    return count