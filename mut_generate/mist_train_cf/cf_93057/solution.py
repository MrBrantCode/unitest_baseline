"""
QUESTION:
Write a function `find_larger_num(num1, num2)` that takes two numbers as input and returns the larger number. If the two numbers are equal, return the message "Both numbers are equal." If both numbers are negative, return the negative number closer to zero. If one number is negative and the other is non-negative, return the number with the larger absolute value. The function should handle integer and floating-point numbers.
"""

def find_larger_num(num1, num2):
    if num1 == num2:
        return "Both numbers are equal."
    elif num1 < 0 and num2 < 0:
        return min(num1, num2, key=abs)
    elif num1 < 0 or num2 < 0:
        return max(num1, num2, key=abs)
    else:
        return max(num1, num2)