"""
QUESTION:
You are given a string of characters, or numbers. Find the minimum number of characters to be inserted into the string in order to obtain a palindrome. 
A palindrome is a word, phrase, number, or other sequence of symbols or elements that reads the same forward or reversed. 

For example, the string abcbd can be transformed into a palindrome ("dabcbad" or "adbcbda"). However, inserting fewer than 2 characters will not produce a palindrome.

Input Format:

First line contains test cases and second line contains an integer 'n' specifying the length of the string, where 3 ≤ n ≤ 20
Second line contains a string of length n. 

Note:

Upper-case and lower-case characters are considered as different. Elements of the string are either English alphabets or numerals.

Output Format:

One line containing the minimum number of insertions required to make the string a palindrome

SAMPLE INPUT
2
5
nitin
7
aabbaab

SAMPLE OUTPUT
0
1
"""

def min_insertions_to_palindrome(s: str) -> int:
    """
    Calculate the minimum number of insertions required to make the given string a palindrome.

    Parameters:
    s (str): The input string.

    Returns:
    int: The minimum number of insertions required.
    """
    if len(s) <= 1:
        return 0
    if s[0] == s[-1]:
        return min_insertions_to_palindrome(s[1:-1])
    else:
        return 1 + min(min_insertions_to_palindrome(s[:-1]), min_insertions_to_palindrome(s[1:]))