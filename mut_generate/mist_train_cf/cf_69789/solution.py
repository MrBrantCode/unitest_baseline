"""
QUESTION:
Write a function `pairwise_sum(a, b, n)` to calculate the sum of pairwise sums of elements from two lists `a` and `b` of size `n`. Analyze the time and space complexity of the function in the best-case, worst-case, and average-case scenarios, and describe the underlying factors that influence the algorithm's behavior. Also, provide a method to optimize the function if possible.
"""

def pairwise_sum(a, b, n):
    """
    Calculate the sum of pairwise sums of elements from two lists a and b of size n.

    Args:
    a (list): The first list of numbers.
    b (list): The second list of numbers.
    n (int): The size of the lists.

    Returns:
    int: The sum of pairwise sums.
    """
    total_sum = 0
    for i in range(n):
        for j in range(n):
            total_sum += a[i] + b[j]
    return total_sum