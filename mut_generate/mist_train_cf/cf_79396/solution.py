"""
QUESTION:
Given a list of integers, write a function `longest_consecutive` that returns the length of the longest consecutive elements sequence in the list. The function should take into account that the input list may contain duplicate elements and may not be sorted. The function should return an integer value representing the length of the longest consecutive sequence.
"""

def longest_consecutive(nums):
    longest_sequence = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence