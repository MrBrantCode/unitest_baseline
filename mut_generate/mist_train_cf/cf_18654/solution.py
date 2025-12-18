"""
QUESTION:
Write a function `find_longest_consecutive_subsequence(arr)` that finds the maximum length of the longest consecutive increasing subsequence in the given array, where the subsequence must include both odd and even numbers and contain at least two elements. The array may contain duplicate numbers. The function should also return the subsequence itself.
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
                
            if current_length > max_length and len(current_subsequence) > 1:
                max_length = current_length
                max_subsequence = current_subsequence
                
    # Checking if the max_subsequence contains at least one odd and one even number
    if max_subsequence:
        odd_nums = [num for num in max_subsequence if num % 2 != 0]
        even_nums = [num for num in max_subsequence if num % 2 == 0]
        if not odd_nums or not even_nums:
            return 0, []
            
    return max_length, max_subsequence