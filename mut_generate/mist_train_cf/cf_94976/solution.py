"""
QUESTION:
Implement a function `square_root(num)` to calculate the square root of a positive integer `num` without using any built-in square root functions. The function should return the square root rounded to the nearest integer. The time complexity of the algorithm should be O(log(log n)).
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