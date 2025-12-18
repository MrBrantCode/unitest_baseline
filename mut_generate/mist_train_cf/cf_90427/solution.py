"""
QUESTION:
Write a function `longest_consecutive_sequence` that takes a list of integers as input and returns the start and end indices of the longest consecutive sequence of unique numbers that are strictly increasing by exactly 1 and contain at least five elements. The function should handle duplicate values in the input list by removing them and considering the longest consecutive sequence with unique elements.
"""

def longest_consecutive_sequence(nums):
    unique_nums = list(set(nums))  # Remove duplicates from the list
    unique_nums.sort()  # Sort the list in ascending order

    start_index = 0
    end_index = 0
    longest_sequence = 0
    current_sequence = 1

    for i in range(len(unique_nums) - 1):
        if unique_nums[i + 1] - unique_nums[i] == 1:
            current_sequence += 1
        else:
            if current_sequence >= 5 and current_sequence > longest_sequence:
                longest_sequence = current_sequence
                start_index = i - current_sequence + 1
                end_index = i
            current_sequence = 1

    # Check the last sequence
    if current_sequence >= 5 and current_sequence > longest_sequence:
        longest_sequence = current_sequence
        start_index = len(unique_nums) - current_sequence
        end_index = len(unique_nums) - 1

    return start_index, end_index