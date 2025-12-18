"""
QUESTION:
You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes). 

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.  

Constraints
 1 ≤ |S| ≤ 100   

Note
String S consists of lowercase English Alphabets only.   

SAMPLE INPUT
aba

SAMPLE OUTPUT
YES
"""

def is_palindrome(s: str) -> str:
    """
    Check if the given string is a palindrome.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    str: "YES" if the string is a palindrome, otherwise "NO".
    """
    reversed_s = "".join(reversed(s))
    if s == reversed_s:
        return "YES"
    else:
        return "NO"