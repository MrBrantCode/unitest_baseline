"""
QUESTION:
Cat Snuke is learning to write characters.
Today, he practiced writing digits 1 and 9, but he did it the other way around.
You are given a three-digit integer n written by Snuke.
Print the integer obtained by replacing each digit 1 with 9 and each digit 9 with 1 in n.

-----Constraints-----
 - 111 \leq n \leq 999
 - n is an integer consisting of digits 1 and 9.

-----Input-----
Input is given from Standard Input in the following format:
n

-----Output-----
Print the integer obtained by replacing each occurrence of 1 with 9 and each occurrence of 9 with 1 in n.

-----Sample Input-----
119

-----Sample Output-----
991

Replace the 9 in the ones place with 1, the 1 in the tens place with 9 and the 1 in the hundreds place with 9. The answer is 991.
"""

def replace_digits(n: str) -> str:
    """
    Replaces each digit '1' with '9' and each digit '9' with '1' in the given three-digit integer string.

    Parameters:
    n (str): A three-digit integer string consisting of digits '1' and '9'.

    Returns:
    str: The integer string obtained by replacing each '1' with '9' and each '9' with '1'.
    """
    replacement_map = {'1': '9', '9': '1'}
    return ''.join(replacement_map[digit] for digit in n)