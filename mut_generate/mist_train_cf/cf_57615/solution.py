"""
QUESTION:
Write a function named `check_perfect_square` that takes one argument, a non-negative integer `num`. The function should return a tuple containing a boolean indicating whether `num` is a perfect square, and either the square root of `num` if it is a perfect square or a tuple of two integers between which the square root of `num` lies if it is not a perfect square. The function should be able to handle very large numbers efficiently.
"""

def entance(num):
    if num < 0:
        return False, None
    if num == 0 or num == 1:
        return True, num
    left, right = 0, num
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == num:
            return True, mid
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    return False, (right, left)