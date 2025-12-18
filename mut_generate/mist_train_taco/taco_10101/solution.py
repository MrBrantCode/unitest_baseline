"""
QUESTION:
This contest is `CODE FESTIVAL`. However, Mr. Takahashi always writes it `CODEFESTIVAL`, omitting the single space between `CODE` and `FESTIVAL`.

So he has decided to make a program that puts the single space he omitted.

You are given a string s with 12 letters. Output the string putting a single space between the first 4 letters and last 8 letters in the string s.

Constraints

* s contains exactly 12 letters.
* All letters in s are uppercase English letters.

Input

The input is given from Standard Input in the following format:


s


Output

Print the string putting a single space between the first 4 letters and last 8 letters in the string s. Put a line break at the end.

Examples

Input

CODEFESTIVAL


Output

CODE FESTIVAL


Input

POSTGRADUATE


Output

POST GRADUATE


Input

ABCDEFGHIJKL


Output

ABCD EFGHIJKL
"""

def insert_space_in_code_festival(s: str) -> str:
    """
    Inserts a single space between the first 4 letters and the last 8 letters of the input string.

    Parameters:
    s (str): A string of exactly 12 uppercase English letters.

    Returns:
    str: The modified string with a single space inserted.
    """
    if len(s) != 12:
        raise ValueError("Input string must be exactly 12 characters long.")
    
    if not s.isupper():
        raise ValueError("Input string must contain only uppercase English letters.")
    
    return s[:4] + ' ' + s[4:]