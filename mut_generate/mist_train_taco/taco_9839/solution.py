"""
QUESTION:
Given is a lowercase English letter C that is not z. Print the letter that follows C in alphabetical order.

-----Constraints-----
 - C is a lowercase English letter that is not z.

-----Input-----
Input is given from Standard Input in the following format:
C

-----Output-----
Print the letter that follows C in alphabetical order.

-----Sample Input-----
a

-----Sample Output-----
b

a is followed by b.
"""

def next_letter(C: str) -> str:
    """
    Returns the letter that follows the given lowercase English letter C in alphabetical order.

    Parameters:
    C (str): A single lowercase English letter that is not 'z'.

    Returns:
    str: The letter that follows C in alphabetical order.
    """
    return chr(ord(C) + 1)