"""
QUESTION:
Create a function named `find_nearest` that takes a sorted list `lst` and a target value as input. The function should return a tuple containing the immediate preceding and following values of the target in the list. If the target is the smallest or largest element in the list, the corresponding preceding or following value should be `None`.
"""

def find_nearest(lst, target):
    # Get all the elements smaller than target
    smaller = [i for i in lst if i < target]
    # Get all the elements larger than target
    larger = [i for i in lst if i > target]

    if smaller:
        # The largest element that is smaller than the target is the preceding value.
        preceding = max(smaller)
    else:
        # If there is no element that is smaller than target, 
        preceding = None
    
    if larger:
        # The smallest element that is larger than the target is the following value.
        following = min(larger)
    else:
        # If there is no element that is larger than target,
        following = None

    return preceding, following