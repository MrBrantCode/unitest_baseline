"""
QUESTION:
Implement a `getPermutation` method that finds the k-th permutation sequence of the numbers from 1 to N. The method should take two parameters, `n` and `k`, where `n` is the total number of elements and `k` is the position of the permutation sequence. The method should return the k-th permutation sequence as a string. The permutation sequence should be 1-indexed, and the method should handle the case where k is 1-indexed.
"""

def getPermutation(n: int, k: int) -> str:
    """
    Finds the k-th permutation sequence of the numbers from 1 to N.

    Args:
    n (int): The total number of elements.
    k (int): The position of the permutation sequence.

    Returns:
    str: The k-th permutation sequence as a string.
    """
    factorials = [1]
    for i in range(1, n):
        factorials.append(factorials[-1] * i)

    numbers = [str(i) for i in range(1, n + 1)]
    k -= 1
    result = ""
    
    for i in range(n - 1, -1, -1):
        index = k // factorials[i]
        k %= factorials[i]
        result += numbers.pop(index)

    return result