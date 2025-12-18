"""
QUESTION:
There are n boys and m girls studying in the class. They should stand in a line so that boys and girls alternated there as much as possible. Let's assume that positions in the line are indexed from left to right by numbers from 1 to n + m. Then the number of integers i (1 ≤ i < n + m) such that positions with indexes i and i + 1 contain children of different genders (position i has a girl and position i + 1 has a boy or vice versa) must be as large as possible. 

Help the children and tell them how to form the line.


-----Input-----

The single line of the input contains two integers n and m (1 ≤ n, m ≤ 100), separated by a space.


-----Output-----

Print a line of n + m characters. Print on the i-th position of the line character "B", if the i-th position of your arrangement should have a boy and "G", if it should have a girl. 

Of course, the number of characters "B" should equal n and the number of characters "G" should equal m. If there are multiple optimal solutions, print any of them.


-----Examples-----
Input
3 3

Output
GBGBGB

Input
4 2

Output
BGBGBB



-----Note-----

In the first sample another possible answer is BGBGBG. 

In the second sample answer BBGBGB is also optimal.
"""

from itertools import repeat, zip_longest

def form_alternating_line(n: int, m: int) -> str:
    """
    Forms a line of children with boys ('B') and girls ('G') alternating as much as possible.

    Parameters:
    - n (int): The number of boys.
    - m (int): The number of girls.

    Returns:
    - str: A string representing the line of children.
    """
    boys = repeat('B', n)
    girls = repeat('G', m)
    
    if n > m:
        pairs = zip_longest(boys, girls, fillvalue=None)
    else:
        pairs = zip_longest(girls, boys, fillvalue=None)
    
    result = (y for x in pairs for y in x if y is not None)
    return ''.join(result)