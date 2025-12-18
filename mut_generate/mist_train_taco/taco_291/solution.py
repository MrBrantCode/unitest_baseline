"""
QUESTION:
Everyone knows that chotu likes palindromic strings. One day, he found 2 ordinary strings s1 and s2. Now he wonders if he could make a palindrome by concatenating s1 and s2 in any order. i.e if s1s2 or s2s1 is a palindrome.

Input

First line of input contains T, denoting number of test cases.
Each test case contains two lines, first line contains string s1 and second line contains string s2.
Output
Print T lines, either "YES" or "NO"(without quotes).

Constrains
1 ≤ T ≤ 1000
1 ≤ |s1|, |s2| ≤ 10000
Both strings contain only lower case letters.

SAMPLE INPUT
2
aba
baba
xy
zw

SAMPLE OUTPUT
YES
NO
"""

def can_form_palindrome(s1: str, s2: str) -> bool:
    """
    Determines if concatenating s1 and s2 in either order results in a palindrome.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    bool: True if the concatenation results in a palindrome, otherwise False.
    """
    temp_str1 = s1 + s2
    temp_str2 = s2 + s1
    
    return temp_str1 == temp_str1[::-1] or temp_str2 == temp_str2[::-1]