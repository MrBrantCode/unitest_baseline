"""
QUESTION:
Write a function `sort_numbers` that takes a list as an argument, which may contain numbers, strings, and nested lists. The function should return a list of unique numbers greater than or equal to 5, in descending order. If a nested list is encountered, the function should flatten the nested list and include its elements in the sorting process. Strings and duplicate numbers should be ignored in the output.
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