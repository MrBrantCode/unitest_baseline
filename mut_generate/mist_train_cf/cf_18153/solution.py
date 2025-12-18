"""
QUESTION:
Write a function named `sum_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function must only use a single loop and cannot use built-in functions or methods to check for even numbers. If the list does not contain any even numbers, the function should return 0.
"""

def entance(numbers):
    # Initialize the sum to 0
    even_sum = 0
    
    # Iterate over each number in the list
    for num in numbers:
        # Check if the number is even
        if num % 2 == 0:
            # Add the even number to the sum
            even_sum += num
    
    # Return the sum of even numbers
    return even_sum