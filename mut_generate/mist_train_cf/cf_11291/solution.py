"""
QUESTION:
Write a function named `find_longest_odd_sequence` that takes an array of integers `nums` as input and returns the longest consecutive sequence of positive odd numbers. The function should iterate over the input array and return a list of integers representing the longest sequence found.
"""

def find_longest_odd_sequence(nums):
    longest_sequence = []
    current_sequence = []
    
    for num in nums:
        if num > 0 and num % 2 != 0:  # Positive odd number
            current_sequence.append(num)
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = []
    
    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence
    
    return longest_sequence