"""
QUESTION:
Given an array of integers `arr` and an integer `difference`, write a function `longestSubsequence(arr, difference)` to compute the length of the longest subsequence within `arr` that forms an arithmetic progression where the difference between consecutive elements in the subsequence is equal to `difference`. The function should return the maximum length of such a subsequence.

Constraints: `1 <= len(arr) <= 10^5` and `-10^4 <= arr[i], difference <= 10^4`.
"""

def longestSubsequence(arr, difference):
    """
    Compute the length of the longest subsequence within arr that forms an arithmetic progression 
    where the difference between consecutive elements in the subsequence is equal to difference.

    Args:
        arr (list): A list of integers.
        difference (int): The difference between consecutive elements in the subsequence.

    Returns:
        int: The maximum length of the longest arithmetic subsequence.
    """
    dp = {}
    for elem in arr:
        if elem - difference in dp:
            dp[elem] = dp[elem - difference] + 1
        else:
            dp[elem] = 1
    return max(dp.values())