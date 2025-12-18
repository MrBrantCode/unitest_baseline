"""
QUESTION:
Implement a function `find_substring(string, substring)` that finds the first index of the `substring` in the `string`. The function should return the index of the first occurrence of the `substring` if found, and -1 otherwise. The function must meet the following requirements: Time Complexity: O(n), where n is the length of the string, and Space Complexity: O(1).
"""

def find_substring(string, substring):
    """
    Finds the first index of the substring in the string.

    Args:
        string (str): The main string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The index of the first occurrence of the substring if found, -1 otherwise.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1).
    """

    n = len(string)
    m = len(substring)

    for i in range(n - m + 1):
        j = 0
        while j < m:
            if string[i + j] != substring[j]:
                break
            j += 1
        if j == m:
            return i

    return -1  # If substring is not found