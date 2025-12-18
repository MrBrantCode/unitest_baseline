"""
QUESTION:
Sachin wants to give a love letter to his girlfriend on valentines day. He 
is having a circular piece of paper of radius "r". 

He wants to use rectangular piece of paper for letter writing whose length and breadth are integers. In how many ways can he do that.

NOTE : Rectangle of a * b and b * a are considered as different rectangles by Sachin.

** Input :**
12

NOTE : You do not need to create a program for this problem you have to write your answers of given input in given code snippet
To see how to submit solution please check this link

SAMPLE INPUT
2

SAMPLE OUTPUT
8

Explanation

No Explanation,, you have to understand yourself.
"""

def count_rectangles_for_letter(radius: int) -> int:
    """
    Counts the number of ways Sachin can use rectangular pieces of paper for letter writing
    on a circular piece of paper of given radius.

    Args:
        radius (int): The radius of the circular piece of paper.

    Returns:
        int: The number of ways to use rectangular pieces of paper.
    """
    import math
    
    # Calculate the maximum side length of the rectangle that can fit in the circle
    max_side = int(math.floor(radius * math.sqrt(2)))
    
    count = 0
    for length in range(1, max_side + 1):
        for breadth in range(1, max_side + 1):
            if length * breadth <= radius ** 2:
                count += 1
    
    return count