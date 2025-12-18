"""
QUESTION:
Create a function `if_can_fly(object, weight_limit, gravity)` that determines whether an object represented by a list can fly under certain conditions. The object can fly if it meets three conditions: its elements form a palindrome list, the cumulative weight of its elements is within the given `weight_limit`, and it can withstand the given `gravity`. The function should return `True` if the object can fly and `False` otherwise. Note that the `gravity` parameter is currently not used in the calculation.
"""

def if_can_fly(object, weight_limit, gravity):
    if object != object[::-1]:
        return False  

    if sum(object) > weight_limit:
        return False      

    return True