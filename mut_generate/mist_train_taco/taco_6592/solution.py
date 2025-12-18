"""
QUESTION:
Suppose you have a string S which has length N and is indexed from 0 to N−1. String R is the reverse of the string S. The string S is funny if the condition |Si−Si−1|=|Ri−Ri−1| is true for every i from 1 to N−1.

(Note: Given a string str, stri denotes the ascii value of the ith character (0-indexed) of str. |x| denotes the absolute value of an integer x)

SAMPLE INPUT
2
acxz
bcxz

SAMPLE OUTPUT
Funny
Not Funny

Explanation

Consider the 1st testcase acxz :

c-a
=
x-z
= 2

z-x
=
a-c
= 2

Consider the 2st testcase bcxz

|c-b| != |x-z|
"""

def is_funny_string(s: str) -> str:
    """
    Determines if a given string is "Funny" based on the condition that the absolute difference 
    between consecutive characters in the string is equal to the absolute difference between 
    consecutive characters in the reversed string.

    Parameters:
    s (str): The input string to be checked.

    Returns:
    str: "Funny" if the string meets the condition, otherwise "Not Funny".
    """
    if len(s) < 2:
        return "Not Funny"
    
    reverse_s = s[::-1]
    
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(reverse_s[i]) - ord(reverse_s[i - 1])):
            return "Not Funny"
    
    return "Funny"