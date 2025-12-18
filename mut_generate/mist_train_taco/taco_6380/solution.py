"""
QUESTION:
For a given array $a_1, a_2, a_3, ... , a_N$ of $N$ elements and an integer $S$, find the smallest sub-array size (smallest window length) where the sum of the sub-array is greater than or equal to $S$. If there is not such sub-array, report 0.

Constraints

* $1 \leq N \leq 10^5$
* $1 \leq S \leq 10^9$
* $1 \leq a_i \leq 10^4$

Input

The input is given in the following format.

$N$ $S$
$a_1$ $a_2$ ... $a_N$

Output

Print the smallest sub-array size in a line.

Examples

Input

6 4
1 2 1 2 3 2


Output

2


Input

6 6
1 2 1 2 3 2


Output

3


Input

3 7
1 2 3


Output

0
"""

def smallest_subarray_with_sum(a: list[int], S: int) -> int:
    n = len(a)
    nows = 0
    ans = 2 << 20  # A large number to represent infinity
    left = 0
    
    for right in range(n):
        nows += a[right]
        while left <= right and right < n:
            if nows >= S:
                ans = min(ans, right - left + 1)
                nows -= a[left]
                left += 1
            else:
                break
    
    return ans % (2 << 20) if ans != (2 << 20) else 0