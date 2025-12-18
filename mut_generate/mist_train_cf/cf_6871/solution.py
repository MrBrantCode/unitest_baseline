"""
QUESTION:
Write a function named `is_perfect_square` that takes an integer `num` greater than or equal to 0 as input and returns a boolean value indicating whether `num` is a perfect square or not. The function should have a time complexity of O(log n), where n is the input number, and should not use any built-in math functions or operators for calculating the square root of the input number, nor any iterative method to find the square root.
"""

def entrance(num):
    if num == 0 or num == 1:
        return True
    
    left = 1
    right = num // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == num:
            return True
        elif square < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return False