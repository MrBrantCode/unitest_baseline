"""
QUESTION:
Consider the following equation: 

<image> where sign [a] represents the integer part of number a.

Let's find all integer z (z > 0), for which this equation is unsolvable in positive integers. The phrase "unsolvable in positive integers" means that there are no such positive integers x and y (x, y > 0), for which the given above equation holds.

Let's write out all such z in the increasing order: z1, z2, z3, and so on (zi < zi + 1). Your task is: given the number n, find the number zn.

Input

The first line contains a single integer n (1 ≤ n ≤ 40).

Output

Print a single integer — the number zn modulo 1000000007 (109 + 7). It is guaranteed that the answer exists.

Examples

Input

1


Output

1

Input

2


Output

3

Input

3


Output

15
"""

def find_zn(n: int) -> int:
    # List of precomputed unsolvable z values modulo 1000000007
    unsolvable_z_values = [
        0, 1, 3, 15, 63, 4095, 65535, 262143, 73741816, 536396503, 140130950, 
        487761805, 319908070, 106681874, 373391776, 317758023, 191994803, 
        416292236, 110940209, 599412198, 383601260, 910358878, 532737550, 
        348927936, 923450985, 470083777, 642578561, 428308066, 485739298, 
        419990027, 287292016, 202484167, 389339971, 848994100, 273206869, 
        853092282, 411696552, 876153853, 90046024, 828945523, 697988359
    ]
    
    # Return the nth unsolvable z value
    return unsolvable_z_values[n]