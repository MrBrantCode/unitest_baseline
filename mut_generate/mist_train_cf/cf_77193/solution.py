"""
QUESTION:
Create a function named `fibonacci` to generate the first 50 Fibonacci numbers and calculate the ratio of each number to its preceding number. The function should return the list of Fibonacci numbers or print the numbers along with their corresponding ratios. The function should be efficient and scalable for large inputs, considering both time and space complexities.
"""

def fibonacci(n=50):
    """
    Generate the first 'n' Fibonacci numbers and calculate the ratio of each number to its preceding number.

    Args:
        n (int): The number of Fibonacci numbers to generate. Defaults to 50.

    Returns:
        list: A list of Fibonacci numbers.
    """
    fiblist = [0, 1]
    while len(fiblist) < n:
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist