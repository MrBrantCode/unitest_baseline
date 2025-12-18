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

def is_funny_string(S: str) -> bool:
    """
    Determines if a given string S is "funny" by checking if the absolute differences 
    of adjacent character ASCII values in the string are equal to the absolute differences 
    of adjacent character ASCII values in the reversed string.

    Parameters:
    S (str): The input string to be checked.

    Returns:
    bool: True if the string is funny, False otherwise.
    """
    N = len(S)
    R = S[::-1]  # Reverse the string
    
    for i in range(1, N):
        if abs(ord(S[i]) - ord(S[i-1])) != abs(ord(R[i]) - ord(R[i-1])):
            return False
    
    return True