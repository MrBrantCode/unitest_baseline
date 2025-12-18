"""
QUESTION:
Implement a function `square_root(num)` that calculates the square root of a given positive number `num` without using any built-in square root function and returns the result rounded to the nearest integer. The function should have a time complexity of O(log(log n)).
"""

def square_root(num):
    if num < 2:
        return num

    left = 0
    right = num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return mid
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1

    return round((left + right) / 2)