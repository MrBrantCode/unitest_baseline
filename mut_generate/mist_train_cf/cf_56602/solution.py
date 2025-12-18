"""
QUESTION:
Design a function `longest_consecutive_subsequence` that takes a list of integers as input and returns the length of the longest subsequence of consecutive integers. The function should handle lists with duplicate elements and should not assume any particular ordering of the input list.
"""

def longest_consecutive_subsequence(lst):
    if not lst:
        return 0
        
    lst = sorted(set(lst))  # remove duplicates and sort
    longest = 1
    current = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1] + 1:  # if current number is one larger than the previous one
            current += 1  # extend current sequence
            longest = max(longest, current)  # update longest sequence
        else:
            current = 1  # reset current sequence
            
    return longest