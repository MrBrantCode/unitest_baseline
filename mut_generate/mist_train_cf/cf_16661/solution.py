"""
QUESTION:
Write a function named fibonacci_even_sum that finds the sum of all even Fibonacci numbers less than the given limit (1 million in this case). The function should generate Fibonacci numbers on the fly without storing the entire sequence. It should return the sum of the even numbers in the sequence.
"""

def fibonacci_even_sum(limit: int) -> int:
    """
    This function generates Fibonacci numbers on the fly and returns the sum of the even numbers in the sequence.

    Args:
    limit (int): The upper limit for the Fibonacci sequence.

    Returns:
    int: The sum of the even numbers in the Fibonacci sequence.
    """
    fibonacci_1 = 1
    fibonacci_2 = 2
    even_sum = 2  

    while fibonacci_2 < limit:
        fibonacci_next = fibonacci_1 + fibonacci_2
        if fibonacci_next % 2 == 0:
            even_sum += fibonacci_next
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_next

    return even_sum