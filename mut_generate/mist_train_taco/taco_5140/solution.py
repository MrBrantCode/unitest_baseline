"""
QUESTION:
You are given a string S consisting of lowercase English letters. We will write down this string, starting a new line after every w letters. Print the string obtained by concatenating the letters at the beginnings of these lines from top to bottom.

Constraints

* 1 \leq w \leq |S| \leq 1000
* S consists of lowercase English letters.
* w is an integer.

Input

Input is given from Standard Input in the following format:


S
w


Output

Print the desired string in one line.

Examples

Input

abcdefgh
3


Output

adg


Input

lllll
1


Output

lllll


Input

souuundhound
2


Output

suudon
"""

def concatenate_line_starts(S: str, w: int) -> str:
    """
    Concatenates the letters at the beginnings of lines formed by splitting the string S after every w letters.

    Parameters:
    - S (str): A string consisting of lowercase English letters.
    - w (int): An integer representing the number of letters after which a new line starts.

    Returns:
    - str: The desired string obtained by concatenating the letters at the beginnings of the lines.
    """
    return ''.join(S[i] for i in range(0, len(S), w))