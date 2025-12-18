"""
QUESTION:
There is data of up to 100 characters per line, consisting of half-width alphabetic character strings. Some lines are symmetric (same whether read from the left edge or the right edge). Create a program that reads this data and outputs the number of symmetric strings in it. Note that lines consisting of only one character are symmetrical.



Input

Multiple strings are given over multiple lines. One string is given for each line. The number of strings does not exceed 50.

Output

Outputs the number of symmetric strings on one line.

Example

Input

abcba
sx
abcddcba
rttrd


Output

2
"""

def count_symmetric_strings(strings):
    """
    Counts the number of symmetric strings in the given list of strings.

    Parameters:
    strings (list of str): A list of strings where each string represents a line of input.

    Returns:
    int: The number of symmetric strings in the input list.
    """
    symmetric_count = 0
    for s in strings:
        if s == s[::-1]:
            symmetric_count += 1
    return symmetric_count