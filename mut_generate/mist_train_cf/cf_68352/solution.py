"""
QUESTION:
Develop a function `isPerfectSquare(num)` that determines whether a given non-negative integer `num` is a perfect square or not. The function should be efficient for large integers and handle exceptions by returning a meaningful message for invalid inputs (numbers less than 0, non-integer inputs).
"""

def isPerfectSquare(num):
    if not isinstance(num, int) or num < 0:
        return "Invalid input. Please enter a non-negative integer."
    else:
        if num == 0 or num == 1:
            return True
        start = 0
        end = num // 2
        while start <= end:
            mid = (start + end) // 2
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr < num:
                start = mid + 1
            else:
                end = mid - 1
        return False