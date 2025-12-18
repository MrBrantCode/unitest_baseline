"""
QUESTION:
Implement two functions, `isSubset` and `largestCommonSubarray`, that take two integer arrays A and B, and their respective lengths m and n. 

The `isSubset` function should return True if all elements of A are present in B, and False otherwise. The `largestCommonSubarray` function should return the largest contiguous subarray common to both A and B.
"""

def isSubset(A, B, m, n):
    """
    Checks if all elements of A are present in B.

    Args:
    A (list): The list to check.
    B (list): The list to check against.
    m (int): The length of A.
    n (int): The length of B.

    Returns:
    bool: True if all elements of A are present in B, False otherwise.
    """
    hashSet = set(B)
    for i in range(m):
        if A[i] not in hashSet:
            return False
    return True


def largestCommonSubarray(A, B, m, n):
    """
    Finds the largest contiguous subarray common to both A and B.

    Args:
    A (list): The first list.
    B (list): The second list.
    m (int): The length of A.
    n (int): The length of B.

    Returns:
    list: The largest contiguous subarray common to both A and B.
    """
    result = []
    lengths = [[0]*(n+1) for _ in range(m+1)]
    longest = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lengths[i][j] = 0
            elif A[i-1] == B[j-1]:
                lengths[i][j] = lengths[i-1][j-1] + 1
                if lengths[i][j] > longest:
                    longest = lengths[i][j]
                    result = A[i-longest: i]
            else:
                lengths[i][j] = 0
    return result