"""
QUESTION:
Create a function `foo(nums_data)` that takes a list of integers `nums_data`, squares each integer and adds 2 to the result, then stores the new values in a list and returns it.
"""

def entrance(nums_data):
    result = []
    for numeric_val in nums_data:
        numeric_val = (numeric_val ** 2) + 2 
        result.append(numeric_val)
    return result