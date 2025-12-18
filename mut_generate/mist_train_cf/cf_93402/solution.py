"""
QUESTION:
Write a function called `longest_consecutive_sequence` that takes a list of integers as input, where the function finds the longest strictly increasing sequence with at least three elements and returns the start and end indices of the sequence.
"""

def longest_consecutive_sequence(nums):
    longest_seq_start = 0
    longest_seq_end = 0
    current_seq_start = 0
    current_seq_end = 0
    longest_seq_length = 0
    current_seq_length = 0
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1] + 1:
            current_seq_end = i
            current_seq_length += 1
        else:
            current_seq_start = i
            current_seq_end = i
            current_seq_length = 1
        
        if current_seq_length >= 3 and current_seq_length > longest_seq_length:
            longest_seq_start = current_seq_start
            longest_seq_end = current_seq_end
            longest_seq_length = current_seq_length
            
    return longest_seq_start, longest_seq_end