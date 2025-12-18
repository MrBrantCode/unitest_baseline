"""
QUESTION:
You drew lottery N times. In the i-th draw, you got an item of the kind represented by a string S_i.
How many kinds of items did you get?

-----Constraints-----
 - 1 \leq N \leq 2\times 10^5
 - S_i consists of lowercase English letters and has a length between 1 and 10 (inclusive).

-----Input-----
Input is given from Standard Input in the following format:
N
S_1
:
S_N

-----Output-----
Print the number of kinds of items you got.

-----Sample Input-----
3
apple
orange
apple

-----Sample Output-----
2

You got two kinds of items: apple and orange.
"""

def count_unique_items(items: list[str]) -> int:
    """
    Counts the number of unique kinds of items drawn in the lottery.

    Parameters:
    - items (list[str]): A list of strings where each string represents an item drawn in the lottery.

    Returns:
    - int: The number of unique kinds of items drawn.
    """
    return len(set(items))