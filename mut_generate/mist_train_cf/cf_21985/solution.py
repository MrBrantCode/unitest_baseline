"""
QUESTION:
Write a function named `max_sum_divisible` that takes a list of positive integers `lst` and an integer `divisor` as input, and returns the maximum possible sum that can be obtained by adding a subset of the integers. The subset must meet two conditions: 
- The sum of the integers in the subset must be divisible by `divisor`.
- The subset must not contain any two consecutive integers from `lst`. 
The function should have a time complexity of O(2^n), where n is the length of `lst`.
"""

def max_sum_divisible(lst, divisor):
    """
    Calculate the maximum possible sum that can be obtained by adding a subset of the integers.
    
    Parameters:
    lst (list): A list of positive integers.
    divisor (int): The divisor that the sum of the subset must be divisible by.
    
    Returns:
    int: The maximum possible sum that can be obtained.
    """
    
    def helper(i, total, prev):
        # Base case: If we've reached the end of the list, return the total if it's divisible by the divisor, otherwise return 0.
        if i == len(lst):
            return total if total % divisor == 0 else 0
        
        # Case 1: Don't include the current element in the subset.
        # We can always do this, regardless of whether the previous element was included.
        case1 = helper(i + 1, total, False)
        
        # Case 2: Include the current element in the subset.
        # We can only do this if the previous element was not included.
        case2 = helper(i + 1, total + lst[i], True) if not prev else 0
        
        # Return the maximum sum between the two cases.
        return max(case1, case2)
    
    return helper(0, 0, False)