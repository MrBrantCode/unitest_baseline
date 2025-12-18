"""
QUESTION:
The GCD table G of size n × n for an array of positive integers a of length n is defined by formula 

<image>

Let us remind you that the greatest common divisor (GCD) of two positive integers x and y is the greatest integer that is divisor of both x and y, it is denoted as <image>. For example, for array a = {4, 3, 6, 2} of length 4 the GCD table will look as follows:

<image>

Given all the numbers of the GCD table G, restore array a.

Input

The first line contains number n (1 ≤ n ≤ 500) — the length of array a. The second line contains n2 space-separated numbers — the elements of the GCD table of G for array a. 

All the numbers in the table are positive integers, not exceeding 109. Note that the elements are given in an arbitrary order. It is guaranteed that the set of the input data corresponds to some array a.

Output

In the single line print n positive integers — the elements of array a. If there are multiple possible solutions, you are allowed to print any of them.

Examples

Input

4
2 1 2 3 4 3 2 6 1 1 2 2 1 2 3 2


Output

4 3 6 2

Input

1
42


Output

42 

Input

2
1 1 1 1


Output

1 1
"""

import collections
import math

def restore_array_from_gcd_table(n, gcd_table):
    """
    Restores the original array 'a' from the given GCD table.

    Parameters:
    n (int): The length of the array 'a'.
    gcd_table (list): A list of n^2 integers representing the GCD table.

    Returns:
    list: The restored array 'a'.
    """
    f = collections.Counter(gcd_table)
    ans = []
    
    for i in range(n):
        now = max(f)
        f[now] -= 1
        for j in ans:
            f[math.gcd(now, j)] -= 2
        ans.append(now)
        f += collections.Counter()
    
    return ans