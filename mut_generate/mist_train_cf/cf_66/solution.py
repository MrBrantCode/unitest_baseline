"""
QUESTION:
Create a function `check_order` that takes a list of numbers as input and returns `True` if the list contains at least one positive number, one negative number, and one zero, in that order. The function should return `False` otherwise. The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def check_order(nums):
    has_positive = False
    has_negative = False
    has_zero = False
    
    for num in nums:
        if num > 0:
            has_positive = True
        elif num < 0:
            if not has_positive:
                return False
            has_negative = True
        else:
            if not has_positive or not has_negative:
                return False
            has_zero = True
            
    return has_positive and has_negative and has_zero