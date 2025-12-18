"""
QUESTION:
A palindrome is a word that reads the same forward and backward. Given a string s, you need to make it a palindrome by adding 0 or more characters to the end of s, and remember, we want the palindrome to be as short as possible.

INPUT

First line is T, the number of test cases. T strings follow, every string s needs to be converted to palindrome.

OUTPUT

Print the shortest possible length of a palindrome that John can generate.

CONSTRAINTS
1 ≤ T ≤ 50
s will contain between 1 and 50 characters,
   inclusive, palindrome can be larger in length. Each character of s
   will be a lowercase letter ('a' - 'z').

SAMPLE INPUT
3
abab
abacaba
qwerty

SAMPLE OUTPUT
5
7
11
"""

def shortest_palindrome_length(s: str) -> int:
    """
    Calculate the shortest possible length of a palindrome that can be generated
    by adding characters to the end of the given string `s`.

    Parameters:
    s (str): The input string that needs to be converted to a palindrome.

    Returns:
    int: The shortest possible length of the palindrome.
    """
    l = len(s)
    for i in range(l):
        a = s[i:]
        b = a[::-1]
        if a == b:
            return l + i
    return 2 * l - 1  # In the worst case, the entire string needs to be mirrored.