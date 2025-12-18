"""
QUESTION:
Create a function called `longest_consecutive_sequence` that takes a list of numbers as input. The function should find the longest strictly increasing sequence of consecutive numbers (with a difference of exactly 1) containing at least 5 elements and return the start and end indices of the sequence. If no such sequence exists, return a message indicating this. The function should assume that the input list contains only integers.
"""

def longest_consecutive_sequence(nums):
    nums_set = set(nums)
    longest_seq = []
    max_length = 0

    for num in nums:
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            if current_length > max_length and current_length >= 5:
                max_length = current_length
                longest_seq = [num, current_num]

    if max_length >= 5:
        return longest_seq
    else:
        return "No consecutive sequence found."