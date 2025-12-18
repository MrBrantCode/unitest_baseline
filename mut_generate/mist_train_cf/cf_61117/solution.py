"""
QUESTION:
Implement the `maxLength` function. 

The function takes a list of strings `arr`, an integer `k`, and a string `c` as input, and returns the maximum length of a concatenation of strings from `arr` that uses at most `k` unique characters and contains the character `c`. 

If no such concatenation exists, return -1. Each string in `arr` is guaranteed to have no duplicate characters. 

Note that `arr` can have at most 15 strings and each string can have at most 10 characters. The function should be implemented with a dynamic programming approach.
"""

def maxLength(arr, k, c):
    """
    Returns the maximum length of a concatenation of strings from `arr` that uses at most `k` unique characters and contains the character `c`.

    Args:
        arr (list[str]): A list of strings.
        k (int): The maximum number of unique characters allowed.
        c (str): The character that the concatenation must contain.

    Returns:
        int: The maximum length of the concatenation. Returns -1 if no such concatenation exists.
    """

    # Filter out strings with duplicate characters
    arr = [word for word in arr if len(set(word)) == len(word)]

    # Initialize dynamic programming table
    dp = [[-1 for _ in range(27)] for _ in range(1 << len(arr))]
    dp[0][0] = 0

    # Iterate over all possible subsets of strings
    for mask in range(1, 1 << len(arr)):
        for unique_char_count in range(27):
            if dp[mask][unique_char_count] == -1:
                continue
            for idx in range(len(arr)):
                if not mask & 1 << idx:
                    # Count the unique characters in the current string
                    chars = collections.Counter(arr[idx])

                    # Check if adding the current string exceeds the unique character limit
                    if len(chars) + unique_char_count <= 26 and all(v == 1 for v in chars.values()) and (c in chars.keys() if unique_char_count > 0 else True):
                        # Update the dynamic programming table
                        new_unique_char_count = unique_char_count + len(chars.keys())
                        dp[mask | 1 << idx][new_unique_char_count] = max(dp[mask | 1 << idx][new_unique_char_count], dp[mask][unique_char_count] + len(arr[idx]))

    # Return the maximum length found
    return max([dp[(1 << len(arr)) - 1][k], -1])