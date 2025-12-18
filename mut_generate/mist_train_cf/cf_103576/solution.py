"""
QUESTION:
Create a test case for the `find_mode(arr)` function that handles a list with multiple modes and an empty list. The function should return the mode of the list, which is the value that appears most frequently. If there are multiple modes, any of them can be returned. If the list is empty, the function should return None.
"""

def find_mode(arr):
    if not arr:
        return None
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    for key, value in count_dict.items():
        if value == max_count:
            return key