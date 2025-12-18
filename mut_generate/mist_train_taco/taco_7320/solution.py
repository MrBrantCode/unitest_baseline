"""
QUESTION:
An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.


-----Input-----

The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.


-----Output-----

Print the minimum number of steps that elephant needs to make to get from point 0 to point x.


-----Examples-----
Input
5

Output
1

Input
12

Output
3



-----Note-----

In the first sample the elephant needs to make one step of length 5 to reach the point x.

In the second sample the elephant can get to point x if he moves by 3, 5 and 4. There are other ways to get the optimal answer but the elephant cannot reach x in less than three moves.
"""

def min_steps_to_friend_house(x: int) -> int:
    """
    Calculate the minimum number of steps an elephant needs to make to reach his friend's house.

    The elephant can move 1, 2, 3, 4, or 5 positions forward in one step.

    Parameters:
    x (int): The coordinate of the friend's house (1 ≤ x ≤ 1,000,000).

    Returns:
    int: The minimum number of steps required to reach the friend's house.
    """
    steps = x // 5
    if x % 5 > 0:
        steps += 1
    return steps