"""
QUESTION:
A palindrome is a word that reads the same forward and backward. Given a string s, you need to make it a palindrome by adding 0 or more characters to the end of s, and remember, we want the palindrome to be as short as possible. 

INPUT

First line is T, the number of test cases.
T strings follow, every string s needs to be converted to palindrome.

OUTPUT

Print the shortest possible length of a palindrome that John can generate.

CONSTRAINTS
1 ≤ T ≤ 50
s will contain between 1 and 50 characters, inclusive, palindrome can be larger in length.
Each character of s will be a lowercase letter ('a' - 'z').

SAMPLE INPUT
3
abab
abacaba
qwerty

SAMPLE OUTPUT
5
7
11

Explanation

CASE 1: "ababa" is the shortest palindrome that we can get.
CASE 2: Already a palindrome.
CASE 3: All characters are different.
"""

def shortest_palindrome_length(s: str) -> int:
    def is_palindrome_suffix(pal: str, start: int) -> bool:
        """Helper function to check if the substring from start to end is a palindrome."""
        return pal[start:] == pal[start:][::-1]

    # Find the longest palindrome suffix
    for i in range(len(s)):
        if is_palindrome_suffix(s, i):
            return len(s) + i
    
    # If no palindrome suffix is found, the entire string needs to be mirrored
    return len(s) * 2 - 1