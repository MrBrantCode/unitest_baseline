"""
QUESTION:
Write a function `find_sum_of_three(array, n)` that checks if the sum of any three numbers in the given array equals the given parameter `n`. The function should return the indices of the three numbers whose sum equals `n`. The function should have a time complexity of O(n^2) and should not use any additional data structures or sorting algorithms.
"""

def find_sum_of_three(array, n):
    """
    Checks if the sum of any three numbers in the given array equals the given parameter `n`.
    Returns the indices of the three numbers whose sum equals `n` if found, otherwise None.

    Time complexity: O(n^2)
    """
    for i in range(len(array)-2):
        left, right = i+1, len(array)-1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == n:
                return [i, left, right]
            elif current_sum < n:
                left += 1
            else:
                right -= 1
    return None