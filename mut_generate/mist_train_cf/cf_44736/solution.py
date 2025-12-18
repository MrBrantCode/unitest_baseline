"""
QUESTION:
Write a Python function called `cubicroot_odd` that takes a list of integers as input. The function should return `True` if the cubic root of every integer in the list is an odd number, and `False` otherwise. The function should not use any built-in math functions or libraries and should handle exceptionally large numbers efficiently. The function should also work with a list of both positive and negative integers.
"""

def cubicroot_odd(nums):
    def check(n): 
        # Initialize start and end for binary search 
        start = 0
        end = max(0, n)

        # Precision for the answer 
        precision = 0.00001

        while (end - start) > precision: 
            mid = (start + end) / 2
            if mid * mid * mid > abs(n): 
                end = mid 
            else: 
                start = mid 

        # negating if n was negative.
        if n < 0:
            start = -start

        #checking cubic root is odd or not
        return int(start) ** 3 == n and int(start) % 2 == 1
    return all(check(n) for n in nums)