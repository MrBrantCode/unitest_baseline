"""
QUESTION:
Add to Array-Form of Integer

Implement a function `addToArrayForm(num, k)` that takes an array `num` representing the digits of an integer in left to right order and an integer `k`, and returns the array-form of the integer `num + k`. The function must not convert the entire `num` or `k` to an integer or string at any point.

Constraints: 
- 1 <= num.length <= 10^4
- 0 <= num[i] <= 9
- num does not contain any leading zeros except for the zero itself.
- 1 <= k <= 10^4
"""

def addToArrayForm(num, k):
    res = []
    for i in range(len(num) - 1, -1, -1):
        k, curr = divmod(k + num[i], 10)
        res.append(curr)
    while k > 0:
        k, curr = divmod(k, 10)
        res.append(curr)
    return res[::-1]