"""
QUESTION:
Extract the odd numbers from a given array, sort them in ascending order, and then square them. The input array will have at most 1000 elements. You cannot use built-in array methods or sorting algorithms. Write a function named `extractOddNumbers` that takes an array as an argument and returns the resulting array of squared odd numbers.
"""

def extractOddNumbers(arr):
    """
    Extract the odd numbers from a given array, sort them in ascending order, 
    and then square them.

    Args:
        arr (list): The input array.

    Returns:
        list: The resulting array of squared odd numbers.
    """

    # Step 1: Extract all the odd numbers from the given array
    odd_numbers = [num for num in arr if num % 2 != 0]

    # Step 2: Sort the extracted odd numbers in ascending order
    for i in range(len(odd_numbers) - 1):
        for j in range(len(odd_numbers) - i - 1):
            if odd_numbers[j] > odd_numbers[j + 1]:
                odd_numbers[j], odd_numbers[j + 1] = odd_numbers[j + 1], odd_numbers[j]

    # Step 3: Square each of the sorted odd numbers
    squared_odd_numbers = [num ** 2 for num in odd_numbers]

    # Step 4: Return the resulting array of squared odd numbers
    return squared_odd_numbers