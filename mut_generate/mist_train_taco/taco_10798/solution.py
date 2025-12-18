"""
QUESTION:
There is a data which provides heights (in meter) of mountains. The data is only for ten mountains.

Write a program which prints heights of the top three mountains in descending order.

Constraints

0 ≤ height of mountain (integer) ≤ 10,000

Input


Height of mountain 1
Height of mountain 2
Height of mountain 3
.
.
Height of mountain 10


Output


Height of the 1st mountain
Height of the 2nd mountain
Height of the 3rd mountain


Examples

Input

1819
2003
876
2840
1723
1673
3776
2848
1592
922


Output

3776
2848
2840


Input

100
200
300
400
500
600
700
800
900
900


Output

900
900
800
"""

def get_top_three_mountains(heights):
    """
    Returns the heights of the top three mountains in descending order.

    Parameters:
    heights (list of int): A list containing the heights of the ten mountains.

    Returns:
    list of int: A list containing the heights of the top three mountains in descending order.
    """
    # Sort the heights in descending order
    sorted_heights = sorted(heights, reverse=True)
    
    # Return the top three heights
    return sorted_heights[:3]