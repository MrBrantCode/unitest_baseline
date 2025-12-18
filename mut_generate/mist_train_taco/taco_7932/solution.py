"""
QUESTION:
Given are three integers A_1, A_2, and A_3.
If A_1+A_2+A_3 is greater than or equal to 22, print bust; otherwise, print win.

-----Constraints-----
 - 1 \leq A_i \leq 13 \ \ (i=1,2,3)
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
A_1 A_2 A_3

-----Output-----
If A_1+A_2+A_3 is greater than or equal to 22, print bust; otherwise, print win.

-----Sample Input-----
5 7 9

-----Sample Output-----
win

5+7+9=21, so print win.
"""

def check_game_result(A_1: int, A_2: int, A_3: int) -> str:
    """
    Determines the result of a game based on the sum of three integers.

    Parameters:
    - A_1 (int): The first integer.
    - A_2 (int): The second integer.
    - A_3 (int): The third integer.

    Returns:
    - str: 'bust' if the sum of A_1, A_2, and A_3 is greater than or equal to 22.
           'win' otherwise.
    """
    if A_1 + A_2 + A_3 >= 22:
        return 'bust'
    else:
        return 'win'