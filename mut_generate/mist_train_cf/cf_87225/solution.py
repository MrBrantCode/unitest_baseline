"""
QUESTION:
Create a function `sort_numbers` that takes a list of elements (possibly containing nested lists) as input and returns a list of unique numbers in descending order, excluding numbers less than 5 and any non-numeric elements.
"""

def sort_numbers(nums):
    temp_list = []
    
    for num in nums:
        if isinstance(num, int) and num >= 5:
            temp_list.append(num)
        elif isinstance(num, list):
            temp_list += sort_numbers(num)
    
    sorted_list = sorted(set(temp_list), reverse=True)
    return sorted_list