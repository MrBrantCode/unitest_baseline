"""
QUESTION:
Write a function named `isPerfectSquare` that takes an integer `num` as input, where `num` is greater than or equal to 0. The function should return a boolean value indicating whether `num` is a perfect square or not, without using built-in math functions or operators for calculating the square root of `num`. The time complexity of the function should be O(log n), where n is the input number.
"""

def isPerfectSquare(num):
    if num < 0:
        return False
    if num == 0:
        return True
    
    # Initialize variables
    start = 1
    end = num
    
    # Use binary search to find the square root
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid
        
        # If the square is equal to the input number, return True
        if square == num:
            return True
        # If the square is greater than the input number, search in the lower half
        elif square > num:
            end = mid - 1
        # If the square is less than the input number, search in the upper half
        else:
            start = mid + 1
    
    # If the loop completes without finding a perfect square, return False
    return False