"""
QUESTION:
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:


Input: 3
Output: [1,3,3,1]


Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

def get_pascals_triangle_row(k: int) -> list[int]:
    res = [1]
    cur = k
    for i in range(k // 2):
        res.append(res[-1] * cur // (i + 1))
        cur -= 1
    if k % 2 == 0:
        res = res + res[:-1][::-1]
    else:
        res = res + res[::-1]
    return res