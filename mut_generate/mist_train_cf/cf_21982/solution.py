"""
QUESTION:
Write a function named `fibonacci(n)` that generates a list of Fibonacci numbers up to the given limit n with a time complexity of O(n). Implement the function using recursion without any loops or iteration. The function should return an empty list for inputs that are negative, non-integer, or greater than 10^6.
"""

def fibonacci(n):
    """
    Generates a list of Fibonacci numbers up to the given limit n with a time complexity of O(n).
    
    Args:
        n (int): The limit up to which the Fibonacci sequence is generated.

    Returns:
        list: A list of Fibonacci numbers up to the given limit n.
    """
    
    if not isinstance(n, int) or n < 0 or n > 10**6:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        _generate_fibonacci(n, fib_list)
        return fib_list

def _generate_fibonacci(n, fib_list):
    """
    Helper function to generate Fibonacci sequence recursively.
    
    Args:
        n (int): The limit up to which the Fibonacci sequence is generated.
        fib_list (list): The list to store the Fibonacci sequence.
    """
    
    if len(fib_list) >= n:
        return
    else:
        fib_list.append(fib_list[-1] + fib_list[-2])
        _generate_fibonacci(n, fib_list)