"""
QUESTION:
Arnab is given a string, but being the evil Lord he is, he has his own whims and fantasies about the string he wants to keep with himself. If he can convert a string into a palindrome by rearranging the characters, he will keep that string, otherwise he will discard that string. You’ve to tell if Arnab will keep that string or not.

Note: A palindrome is a word which reads the same backward or forward. 

Input: 
The first line of input contains the number of test cases T. Each test case contains a single string S.

Output:
For each test case print Yes if Arnab can convert string into a palindrome by rearranging the characters else print No.

Constraints:
1 ≤ Number of test cases, T ≤ 10
1 ≤ |Length of String S| ≤ 100

SAMPLE INPUT
3
code
pop
abbSAMPLE OUTPUT
No
Yes
Yes
"""

def can_form_palindrome(s: str) -> bool:
    """
    Determines if a given string can be rearranged into a palindrome.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    bool: True if the string can be rearranged into a palindrome, otherwise False.
    """
    char_count = [0] * 26  # Initialize a list to count occurrences of each character
    for char in s:
        char_count[ord(char) - ord('a')] += 1
    
    odd_count = 0  # Count of characters with odd occurrences
    for count in char_count:
        if count % 2 != 0:
            odd_count += 1
    
    # A string can be rearranged into a palindrome if at most one character has an odd count
    return odd_count <= 1