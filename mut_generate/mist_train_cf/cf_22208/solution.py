"""
QUESTION:
Write a function `extractAndSortOddNumbers` that takes an array of at most 1000 integers as input, extracts the odd numbers, sorts them in ascending order without using built-in sorting algorithms, squares each of the sorted odd numbers, and returns the resulting array.
"""

def extractAndSortOddNumbers(arr):
    """
    This function takes an array of integers, extracts the odd numbers, sorts them in ascending order,
    squares each of the sorted odd numbers, and returns the resulting array.
    
    Parameters:
    arr (list): A list of integers
    
    Returns:
    list: A list of squared odd numbers in ascending order
    """
    
    # Extract odd numbers from the input array
    odd_numbers = [num for num in arr if num % 2 != 0]
    
    # Sort the odd numbers in ascending order using bubble sort
    for i in range(len(odd_numbers)):
        for j in range(i + 1, len(odd_numbers)):
            if odd_numbers[i] > odd_numbers[j]:
                odd_numbers[i], odd_numbers[j] = odd_numbers[j], odd_numbers[i]
    
    # Square each of the sorted odd numbers
    squared_odd_numbers = [num ** 2 for num in odd_numbers]
    
    return squared_odd_numbers