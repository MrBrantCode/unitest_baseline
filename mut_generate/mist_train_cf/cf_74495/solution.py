"""
QUESTION:
Write a function `determine_big_o` that determines the time complexity of an algorithm using Big O notation. The function should take as input a function `f(n)` representing the number of basic operations required by an algorithm for a given input of size `n`, and return the time complexity of the algorithm in Big O notation. The function should return a string representing the time complexity, such as 'O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n^2)', etc.
"""

def determine_big_o(f, n_max=1000):
    """
    Determine the time complexity of an algorithm using Big O notation.

    Args:
    f (function): A function representing the number of basic operations required by an algorithm for a given input of size n.
    n_max (int): The maximum input size to test. Defaults to 1000.

    Returns:
    str: The time complexity of the algorithm in Big O notation.
    """

    # Test the function with different input sizes
    n_values = [2**i for i in range(10)]
    results = [f(n) for n in n_values]

    # Check for O(1)
    if all(result == results[0] for result in results):
        return 'O(1)'

    # Check for O(log n)
    log_n_values = [i for i in range(10)]
    if all(result == log_n_value for result, log_n_value in zip(results, log_n_values)):
        return 'O(log n)'

    # Check for O(n)
    if all(result == n for result, n in zip(results, n_values)):
        return 'O(n)'

    # Check for O(n log n)
    n_log_n_values = [n * log_n for n, log_n in zip(n_values, log_n_values)]
    if all(result == n_log_n for result, n_log_n in zip(results, n_log_n_values)):
        return 'O(n log n)'

    # Check for O(n^2)
    n_squared_values = [n**2 for n in n_values]
    if all(result == n_squared for result, n_squared in zip(results, n_squared_values)):
        return 'O(n^2)'

    # Check for O(2^n)
    two_pow_n_values = [2**n for n in n_values]
    if all(result == two_pow_n for result, two_pow_n in zip(results, two_pow_n_values)):
        return 'O(2^n)'

    # If none of the above, return a generic result
    return 'O(f(n))'