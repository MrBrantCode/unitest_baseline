"""
QUESTION:
Write a function `prime_factors(n)` that takes an integer `n` as input and returns a dictionary where the keys are the distinct prime factors of `n` and the values are their respective frequencies. The function should be efficient in terms of time and space complexity. Additionally, implement a function `prime_factors_multiple_numbers(numbers)` that takes a list of integers as input and returns a dictionary where each key is a number from the input list and the value is the dictionary of prime factors for that number.
"""

def prime_factors(n):
    """
    This function takes an integer n as input and returns a dictionary where the keys are the distinct prime factors of n and the values are their respective frequencies.
    
    Parameters:
    n (int): The number to find prime factors for.
    
    Returns:
    dict: A dictionary with prime factors as keys and their frequencies as values.
    """
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def prime_factors_multiple_numbers(numbers):
    """
    This function takes a list of integers as input and returns a dictionary where each key is a number from the input list and the value is the dictionary of prime factors for that number.
    
    Parameters:
    numbers (list): A list of integers to find prime factors for.
    
    Returns:
    dict: A dictionary with numbers as keys and their prime factors as values.
    """
    result = {}
    for number in numbers:
        result[number] = prime_factors(number)
    return result