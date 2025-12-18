"""
QUESTION:
You have an array a with length n, you can perform operations. Each operation is like this: choose two adjacent elements from a, say x and y, and replace one of them with gcd(x, y), where gcd denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

What is the minimum number of operations you need to make all of the elements equal to 1?

Input

The first line of the input contains one integer n (1 ≤ n ≤ 2000) — the number of elements in the array.

The second line contains n space separated integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the elements of the array.

Output

Print -1, if it is impossible to turn all numbers to 1. Otherwise, print the minimum number of operations needed to make all numbers equal to 1.

Examples

Input

5
2 2 3 4 6


Output

5


Input

4
2 4 6 8


Output

-1


Input

3
2 6 9


Output

4

Note

In the first sample you can turn all numbers to 1 using the following 5 moves:

  * [2, 2, 3, 4, 6]. 
  * [2, 1, 3, 4, 6]
  * [2, 1, 3, 1, 6]
  * [2, 1, 1, 1, 6]
  * [1, 1, 1, 1, 6]
  * [1, 1, 1, 1, 1]



We can prove that in this case it is not possible to make all numbers one using less than 5 moves.
"""

import math

def min_operations_to_make_all_ones(n, a):
    # Check if there is already a 1 in the array
    x = [1 for x in a if x == 1]
    x_count = len(x)
    
    if x_count >= 1:
        return n - x_count
    
    # Initialize the answer to a large value
    ans = n
    
    # Find the minimum subarray length that has a gcd of 1
    for i in range(n):
        g = a[i]
        for j in range(i, n):
            g = math.gcd(g, a[j])
            if g == 1:
                ans = min(ans, j - i)
                break
    
    # If no subarray with gcd 1 was found, return -1
    if ans == n:
        return -1
    
    # Otherwise, return the minimum number of operations
    return ans + n - 1