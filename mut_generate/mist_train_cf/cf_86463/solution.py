"""
QUESTION:
Compute the exact square root of a given number using basic arithmetic operations (addition, subtraction, multiplication, and division) without using built-in square root functions or libraries, and without iterative methods like Newton's method. The function should be named `sqrt` and take an integer `x` as input. The time complexity of the solution should be less than or equal to O(log n), where n is the given number.
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
            ans = mid
            start = mid + 1
        else:
            end = mid - 1

    return ans