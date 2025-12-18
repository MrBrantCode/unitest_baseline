"""
QUESTION:
Find the maximum length of the longest consecutive increasing subsequence in an array where the subsequence must include both odd and even numbers. The function should also return the subsequence itself. The array may contain duplicate numbers.

Function name: find_longest_consecutive_subsequence
Input: A list of integers
Restriction: The subsequence must include both odd and even numbers.
"""

def find_longest_consecutive_subsequence(arr):
    arr_set = set(arr)  # Convert array to set for faster lookup
    
    max_length = 0
    max_subsequence = []
    
    for num in arr:
        if num - 1 not in arr_set:  # Check if num is the start of a subsequence
            current_length = 0
            current_subsequence = []
            
            while num in arr_set:  # Continue adding numbers to the subsequence
                current_length += 1
                current_subsequence.append(num)
                num += 1
                
            if (current_length > max_length) and (len(current_subsequence) > 1) and (any(x % 2 == 0 for x in current_subsequence) and any(x % 2 != 0 for x in current_subsequence)):
                max_length = current_length
                max_subsequence = current_subsequence
    
    return max_length, max_subsequence