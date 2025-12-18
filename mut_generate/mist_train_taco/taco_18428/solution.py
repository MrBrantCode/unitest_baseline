"""
QUESTION:
Snuke has a grid consisting of three squares numbered 1, 2 and 3.
In each square, either 0 or 1 is written. The number written in Square i is s_i.
Snuke will place a marble on each square that says 1.
Find the number of squares on which Snuke will place a marble.

-----Constraints-----
 - Each of s_1, s_2 and s_3 is either 1 or 0.

-----Input-----
Input is given from Standard Input in the following format:
s_{1}s_{2}s_{3}

-----Output-----
Print the answer.

-----Sample Input-----
101

-----Sample Output-----
2

 - A marble will be placed on Square 1 and 3.
"""

def count_marbles(s: str) -> int:
    """
    Counts the number of squares on which Snuke will place a marble.

    Parameters:
    s (str): A string of length 3, where each character is either '0' or '1'.

    Returns:
    int: The number of squares on which Snuke will place a marble.
    """
    count = 0
    for char in s:
        if char == '1':
            count += 1
    return count