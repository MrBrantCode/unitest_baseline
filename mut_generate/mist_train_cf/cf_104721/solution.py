"""
QUESTION:
Create a function `compare_lists(nums, strings)` that takes a list of numbers and a list of strings as input. The function should return the highest number or the string with the highest alphabetical order. If one list is empty, return the highest value from the other list. If both lists are empty, return None.
"""

def entrance(nums, strings):
    if len(nums) == 0 and len(strings) == 0:
        return None
    elif len(nums) == 0:
        return max(strings)
    elif len(strings) == 0:
        return max(nums)
    else:
        max_num = max(nums)
        max_string = max(strings)
        if str(max_num) > max_string:
            return max_num
        else:
            return max_string