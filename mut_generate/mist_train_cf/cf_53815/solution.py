"""
QUESTION:
Given a unique array of positive integers `nums` with length between 1 and 1000, write a function named `solve` that calculates the count of quadruplets `(a, b, c, d)` where `a`, `b`, `c`, and `d` are distinct elements of `nums` and `a * b == c * d`, and return the count of such quadruplets. The function should have a time complexity of O(n^2) and space complexity of O(n^2), where n is the length of `nums`.
"""

def solve(nums):
    count = 0
    dict = {}
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            if product not in dict:
                dict[product] = 1
            else:
                count += dict[product]
                dict[product] += 1
    return count * 4