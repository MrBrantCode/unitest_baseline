"""
QUESTION:
Create a function `prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers. The function should exclude non-prime numbers and zero and one are considered non-prime numbers. The function should not modify the original list. The output list should only include integers that are prime numbers from the input list.
"""

def prime_numbers(lst):
    """
    Returns a new list containing only the prime numbers from the input list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A list of prime numbers.
    """
    return [num for num in lst if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1))]