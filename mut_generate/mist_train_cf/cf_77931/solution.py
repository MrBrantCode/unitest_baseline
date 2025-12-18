"""
QUESTION:
Design a function `subset_sum` that takes a list of numbers and a target number as input, and returns all unique subsets of the list whose sum equals the target number. The function should optimize the number of operations performed. The input list will have a length of at least 2 and at most 10^3, and the target number will be an integer within the range 1 to 10^6.
"""

def subset_sum(numbers, target, partial=[]):
    """
    Returns all unique subsets of the list whose sum equals the target number.

    Args:
        numbers (list): A list of numbers.
        target (int): The target sum.
        partial (list, optional): A partial subset. Defaults to [].

    Yields:
        list: A subset of numbers that sums up to the target.
    """
    s = sum(partial)
    if s == target: 
        yield partial
    if s >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i+1:]
        yield from subset_sum(remaining, target, partial + [n])