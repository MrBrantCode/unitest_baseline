"""
QUESTION:
Write a function `find_max_sum` that takes a list of integers as input and returns the maximum sum of any subsequence in the list. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the list.
"""

def find_max_sum(lst):
    max_sum = 0
    curr_sum = 0

    for num in lst:
        curr_sum += num
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum