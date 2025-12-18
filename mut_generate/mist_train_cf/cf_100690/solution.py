"""
QUESTION:
Calculate the time complexities of two given algorithms, sum_n and sum_n_squared, where sum_n calculates the sum of integers from 0 to n and sum_n_squared calculates the sum of products of all pairs of integers from 0 to n. Assume the input size is represented as 'n'. Provide the time complexity of each algorithm using Big-O notation. The algorithms are as follows:

- sum_n(n): 
  - Initialize sum to 0.
  - For each integer i from 0 to n-1, add i to sum.

- sum_n_squared(n): 
  - Initialize sum to 0.
  - For each integer i from 0 to n-1, for each integer j from 0 to n-1, add i * j to sum.
"""

def sum_n(n):
    """Calculates the sum of integers from 0 to n"""
    total_sum = 0
    for i in range(n):
        total_sum += i
    return total_sum

def sum_n_squared(n):
    """Calculates the sum of products of all pairs of integers from 0 to n"""
    total_sum = 0
    for i in range(n):
        for j in range(n):
            total_sum += i * j
    return total_sum