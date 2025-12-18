"""
QUESTION:
We have a sequence of length N, a = (a_1, a_2, ..., a_N).
Each a_i is a positive integer.
Snuke's objective is to permute the element in a so that the following condition is satisfied:
 - For each 1 ≤ i ≤ N - 1, the product of a_i and a_{i + 1} is a multiple of 4.
Determine whether Snuke can achieve his objective.

-----Constraints-----
 - 2 ≤ N ≤ 10^5
 - a_i is an integer.
 - 1 ≤ a_i ≤ 10^9

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 a_2 ... a_N

-----Output-----
If Snuke can achieve his objective, print Yes; otherwise, print No.

-----Sample Input-----
3
1 10 100

-----Sample Output-----
Yes

One solution is (1, 100, 10).
"""

def can_permute_for_multiple_of_4(N, a):
    """
    Determines if Snuke can permute the elements in the sequence `a` such that
    for each 1 ≤ i ≤ N - 1, the product of a_i and a_{i + 1} is a multiple of 4.

    Parameters:
    - N (int): The length of the sequence.
    - a (list of int): The sequence of positive integers.

    Returns:
    - bool: True if Snuke can achieve his objective, False otherwise.
    """
    b1, b2, b4 = 0, 0, 0
    
    for i in a:
        if i % 2 != 0:
            b1 += 1
        elif i % 4 == 0:
            b4 += 1
        else:
            b2 += 1
    
    if b1 <= b4:
        return True
    elif b1 <= b4 + 1 and not b2:
        return True
    else:
        return False