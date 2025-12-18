"""
QUESTION:
Write a function `find_anomalous` that takes in a nested list of integers `arr` and a prime number `prime`, and returns the first integer in `arr` whose count is not divisible by `prime`. If no such integer exists, return `None`. The function should handle nested lists of arbitrary depth and have optimal time complexity.
"""

def find_anomalous(arr, prime):
    """Find the debut integer with a non-divisible count"""
    counts = {}
    try:
        _find_anomalous_recursive(arr, prime, counts)
    except AnomalousNumberFound as e:
        return e.value
    return None

class AnomalousNumberFound(Exception):
    def __init__(self, value):
        self.value = value

def _find_anomalous_recursive(arr, prime, counts):
    """Recursively walk through the elements, updating counts
    and checking for the debut anomaly"""
    for i in arr:
        if isinstance(i, list):
            _find_anomalous_recursive(i, prime, counts)
        else:
            counts[i] = counts.get(i, 0) + 1
            if counts[i] % prime != 0:
                raise AnomalousNumberFound(i)