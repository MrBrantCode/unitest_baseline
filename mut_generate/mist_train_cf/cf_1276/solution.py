"""
QUESTION:
Write a function `sum_even_elements` that takes an array of at least 10 positive integers as input, sums all the even elements, multiplies the sum by the first element in the array, and returns the final result.
"""

def sum_even_elements(arr):
    # Initialize sum variable and multiply it by the first element in the array
    result = 0
    
    # Iterate over each element in the array
    for num in arr:
        # Check if the element is even
        if num % 2 == 0:
            # Add the even element to the sum
            result += num
    
    # Return the final result, which is the sum multiplied by the first element
    return result * arr[0]