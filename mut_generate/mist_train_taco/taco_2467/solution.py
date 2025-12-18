"""
QUESTION:
AtCoDeer the deer recently bought three paint cans.
The color of the one he bought two days ago is a, the color of the one he bought yesterday is b, and the color of the one he bought today is c.
Here, the color of each paint can is represented by an integer between 1 and 100, inclusive.
Since he is forgetful, he might have bought more than one paint can in the same color.
Count the number of different kinds of colors of these paint cans and tell him.

-----Constraints-----
 - 1≦a,b,c≦100

-----Input-----
The input is given from Standard Input in the following format:
a b c

-----Output-----
Print the number of different kinds of colors of the paint cans.

-----Sample Input-----
3 1 4

-----Sample Output-----
3

Three different colors: 1, 3, and 4.
"""

def count_unique_colors(a: int, b: int, c: int) -> int:
    """
    Counts the number of unique colors among three paint cans.

    Parameters:
    a (int): The color of the paint can bought two days ago.
    b (int): The color of the paint can bought yesterday.
    c (int): The color of the paint can bought today.

    Returns:
    int: The number of unique colors among the three paint cans.
    """
    unique_colors = {a, b, c}
    return len(unique_colors)