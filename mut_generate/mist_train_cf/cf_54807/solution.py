"""
QUESTION:
Write a function `enhanced_nums(a, b, c, d, e, s)` that accepts five positive integers `a, b, c, d, e` and a list `s` containing positive integers. The function should return a tuple containing two integers. 

The first integer should be the largest integer within the range `[a, b]` inclusive that is divisible evenly by both `c` and any number in the given list `s` without any remainder. If no such integer is found in the range, return -1.

The second integer should be the smallest integer within the range `[d, e]` inclusive that is divisible evenly by both `c` and any number in the given list `s` without any remainder. If no such integer is found in the range, return -1.
"""

def enhanced_nums(a, b, c, d, e, s):
    def check_range(start, end, div, s, reverse=False):
        nums = range(start, end + 1) if not reverse else range(end, start - 1, -1)
        for num in nums:
            if num % div == 0 and any(num % si == 0 for si in s):
                return num
        return -1

    return check_range(a, b, c, s, reverse=True), check_range(d, e, c, s)