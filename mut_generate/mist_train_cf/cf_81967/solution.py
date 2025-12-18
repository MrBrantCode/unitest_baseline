"""
QUESTION:
Write a function `numPairs(arr)` that takes an even-length integer array `arr` as input and returns the number of possible arrangements that satisfy the condition `arr[2 * i + 1] = 2 * arr[2 * i]` for every `0 <= i < len(arr) / 2`. If no such arrangement is possible, return -1.

The length of the input array `arr` is even and satisfies `0 <= arr.length <= 3 * 10^4`. Each element in the array is an integer that satisfies `-10^5 <= arr[i] <= 10^5`. The order of the pairs does not matter, but the order within a pair does matter.
"""

from collections import Counter

def numPairs(arr):
    """
    Calculate the number of possible arrangements in an array where every pair 
    satisfies the condition arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

    Args:
    arr (list): An even-length integer array.

    Returns:
    int: The number of possible arrangements, or -1 if no arrangement is possible.
    """
    
    n = len(arr)
    
    if n == 0: 
        return 0
    
    arr.sort(key=abs) # Sort array with absolute values
    
    freq = Counter(arr) # Get frequency of each element
    
    for num in arr:
        if freq[num] == 0: 
            continue
        if freq[num * 2] <= 0: 
            return -1
        freq[num] -= 1
        freq[num * 2] -= 1

    return 1 if n // 2 <= 0 else n // 2