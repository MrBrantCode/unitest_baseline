"""
QUESTION:
Write a function `separate_even_odd` that takes a list of integers as input and returns or prints the reversed list and two separate lists for even and odd numbers in descending order. The function should achieve this in a single pass and without using built-in functions for reversing or sorting. The even and odd lists should be in the same order as they appear in the reversed input list.
"""

def separate_even_odd(numbers):
    """
    Reverses the input list and separates the numbers into even and odd lists.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the reversed list and two separate lists for even and odd numbers.
    """

    # Initialize empty lists to store reversed numbers, even numbers, and odd numbers
    reversed_numbers = []
    even_numbers = []
    odd_numbers = []

    # Iterate the input list in reverse to achieve the reverse order
    for i in range(len(numbers)-1, -1, -1):
        
        # Append the current number to the reversed list
        reversed_numbers.append(numbers[i])
        
        # Check if the current number is even
        if numbers[i] % 2 == 0:
            # If even, append it to the even list
            even_numbers.append(numbers[i])
        else:
            # If odd, append it to the odd list
            odd_numbers.append(numbers[i])
    
    # Return the reversed list and the even and odd lists
    return reversed_numbers, even_numbers, odd_numbers