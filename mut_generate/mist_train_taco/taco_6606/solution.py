"""
QUESTION:
Takahashi loves palindromes. Non-palindromic strings are unacceptable to him. Each time he hugs a string, he can change one of its characters to any character of his choice.
Given is a string S. Find the minimum number of hugs needed to make S palindromic.

-----Constraints-----
 - S is a string consisting of lowercase English letters.
 - The length of S is between 1 and 100 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the minimum number of hugs needed to make S palindromic.

-----Sample Input-----
redcoder

-----Sample Output-----
1

For example, we can change the fourth character to o and get a palindrome redooder.
"""

def min_hugs_to_palindrome(S: str) -> int:
    """
    Calculate the minimum number of character changes (hugs) needed to make the string S a palindrome.

    Parameters:
    S (str): The input string consisting of lowercase English letters.

    Returns:
    int: The minimum number of hugs needed to make S a palindrome.
    """
    S = list(S)  # Convert the string to a list of characters
    d = 0
    for i in range(len(S) // 2):
        if S[i] != S[len(S) - i - 1]:
            d += 1
    return d