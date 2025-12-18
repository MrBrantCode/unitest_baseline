"""
QUESTION:
Emuskald is a well-known illusionist. One of his trademark tricks involves a set of magical boxes. The essence of the trick is in packing the boxes inside other boxes.

From the top view each magical box looks like a square with side length equal to 2k (k is an integer, k ≥ 0) units. A magical box v can be put inside a magical box u, if side length of v is strictly less than the side length of u. In particular, Emuskald can put 4 boxes of side length 2k - 1 into one box of side length 2k, or as in the following figure:

<image>

Emuskald is about to go on tour performing around the world, and needs to pack his magical boxes for the trip. He has decided that the best way to pack them would be inside another magical box, but magical boxes are quite expensive to make. Help him find the smallest magical box that can fit all his boxes.

Input

The first line of input contains an integer n (1 ≤ n ≤ 105), the number of different sizes of boxes Emuskald has. Each of following n lines contains two integers ki and ai (0 ≤ ki ≤ 109, 1 ≤ ai ≤ 109), which means that Emuskald has ai boxes with side length 2ki. It is guaranteed that all of ki are distinct.

Output

Output a single integer p, such that the smallest magical box that can contain all of Emuskald’s boxes has side length 2p.

Examples

Input

2
0 3
1 5


Output

3


Input

1
0 4


Output

1


Input

2
1 10
2 2


Output

3

Note

Picture explanation. If we have 3 boxes with side length 2 and 5 boxes with side length 1, then we can put all these boxes inside a box with side length 4, for example, as shown in the picture.

In the second test case, we can put all four small boxes into a box with side length 2.
"""

from math import ceil, log, fabs

def find_smallest_box_size(boxes):
    """
    Finds the smallest magical box size that can contain all given boxes.

    Parameters:
    boxes (list of tuples): A list where each tuple contains two integers (ki, ai),
                            representing the side length exponent ki and the number of boxes ai.

    Returns:
    int: The smallest side length exponent p such that the smallest magical box has side length 2^p.
    """
    v = 0
    for ki, ai in boxes:
        k = ceil(fabs(log(ai, 4)))
        if k == 0:
            k = 1
        if k + ki > v:
            v = k + ki
    return v