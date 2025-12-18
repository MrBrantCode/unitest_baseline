"""
QUESTION:
Create a function `find_pair(numbers, target)` that takes a list of integers `numbers` and an integer `target` as input, and returns a tuple of two numbers from the list whose sum equals the `target`. The pair should consist of distinct elements, meaning they should have unique indices in the list.
"""

def find_pair(numbers, target):
    # Dictionary to store the differences between target and elements
    diff_dict = {}
    
    for index, num in enumerate(numbers):
        diff = target - num
        if diff in diff_dict:
            return (diff, num)
        else:
            diff_dict[num] = index
    return None