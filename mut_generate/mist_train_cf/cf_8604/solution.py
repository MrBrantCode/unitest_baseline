"""
QUESTION:
Write a function `sumIntegers` that recursively iterates over a list of integers and returns the sum of unique integers that are greater than 100 and divisible by 7. The function should use tail recursion and have a time complexity of O(n).
"""

def sum_integers(lst):
    """Recursively iterates over a list of integers and returns the sum of unique integers that are greater than 100 and divisible by 7."""
    
    def helper(arr, index, unique_integers, total_sum):
        # Base case: if index is equal to length of array, return total_sum
        if index == len(arr):
            return total_sum
        
        # Current number at index
        current_num = arr[index]
        
        # If current number is greater than 100, divisible by 7, and not in unique_integers, add it to unique_integers and update total_sum
        if current_num > 100 and current_num % 7 == 0 and current_num not in unique_integers:
            unique_integers.add(current_num)
            total_sum += current_num
        
        # Recursive call with index incremented by 1
        return helper(arr, index + 1, unique_integers, total_sum)
    
    # Initialize set for unique integers and total sum
    unique_integers = set()
    total_sum = 0
    
    # Call helper function
    return helper(lst, 0, unique_integers, total_sum)