"""
QUESTION:
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left. 

NOTE: String letters are case-sensitive.

Input Format  

The first line of input contains the original string. The next line contains the substring.

Constraints  

$1\leq len(string)\leq200$ 

Each character in the string is an ascii character. 

Output Format 

Output the integer number indicating the total number of occurrences of the substring in the original string. 

Sample Input

ABCDCDC
CDC

Sample Output

2

Concept

Some string processing examples, such as these, might be useful. 

There are a couple of new concepts: 

In Python, the length of a string is found by the function len(s), where $\boldsymbol{\mathrm{~S~}}$ is the string. 

To traverse through the length of a string, use a for loop:  

for i in range(0, len(s)):
    print (s[i])

A range function is used to loop over some length: 

range (0, 5)

Here, the range loops over $\mbox{o}$ to $\begin{array}{c}A\end{array}$. $5$ is excluded.
"""

def count_substring_occurrences(original_string: str, substring: str) -> int:
    """
    Counts the number of times a substring occurs in the original string.

    Parameters:
    - original_string (str): The original string in which to search for the substring.
    - substring (str): The substring to count occurrences of.

    Returns:
    - int: The number of times the substring occurs in the original string.
    """
    count = 0
    sub_len = len(substring)
    for i in range(len(original_string) - sub_len + 1):
        if original_string[i:i + sub_len] == substring:
            count += 1
    return count