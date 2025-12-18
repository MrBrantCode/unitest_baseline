"""
QUESTION:
Write a function `sqrt(x)` to compute the exact square root of a given number `x` using only basic arithmetic operations (addition, subtraction, multiplication, and division) with a time complexity of O(log n) or less, where `n` is the input number `x`. The function should not use any built-in square root functions or libraries, and it should not use any iterative methods to approximate the square root.
"""

def sqrt(x):
    if x == 0 or x == 1:
        return x

    start = 1
    end = x
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1

    return ans