"""
QUESTION:
Write a function `find_longest_odd_sequence` that takes a list of integers as input and returns the longest consecutive sequence of positive odd numbers in the list. The input list may contain both positive and negative numbers, and the function should return an empty list if no positive odd numbers are found.
"""

def find_longest_odd_sequence(nums):
    longest_sequence = []
    current_sequence = []
    
    for num in nums:
        if num > 0 and num % 2 != 0:  
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = []
    
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    
    return longest_sequence