"""
QUESTION:
Write a function `isPerfectSquare` and `findSquareRoot` that determines whether a given non-negative integer `num` is a perfect square or not and calculates the square root of the number without using any built-in functions or libraries. The time complexity of the solution should be O(log n), where n is the given number. The `findSquareRoot` function should return the integer part of the square root if the given number is not a perfect square.
"""

def find_square_root(num):
    """This function determines whether a given non-negative integer is a perfect square or not and calculates the square root of the number.
    
    Args:
        num (int): The given number.
    
    Returns:
        tuple: A boolean indicating whether the number is a perfect square and the integer part of the square root.
    """
    
    if num < 0:
        return False, None
    if num == 0 or num == 1:
        return True, num

    left, right = 0, num
    ans = 0

    while left <= right:
        mid = (left + right) // 2
        if mid*mid == num:
            return True, mid
        elif mid*mid < num:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return False, ans