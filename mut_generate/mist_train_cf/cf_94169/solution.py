"""
QUESTION:
Write a function `find_max_sum_pair(arr)` that takes an array of integers as input and returns the two distinct elements with the maximum sum. If multiple pairs have the same maximum sum, return the pair with the smallest first element. The function must have a time complexity of O(n) and a space complexity of O(n).
"""

def find_max_sum_pair(arr):
    max_sum = float('-inf')
    max_pair = (0, 0)
    sum_dict = {}

    for num in arr:
        if num not in sum_dict:
            sum_dict[num] = num
        else:
            sum_dict[num] += num

        if sum_dict[num] > max_sum:
            max_sum = sum_dict[num]
            max_pair = (num, num)

    return max_pair