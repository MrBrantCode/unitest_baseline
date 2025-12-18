"""
QUESTION:
Write a function called `get_average` that takes a list of elements as input, calculates the average of all the integers and floats in the list (excluding strings, nested lists, and dictionaries), and returns the result. The function should handle nested lists and dictionaries by recursively calling itself on these elements, but only include their numerical values in the calculation. The time complexity of the function should be O(n), where n is the total number of elements in the list, including nested lists and dictionaries. You should not use built-in functions or libraries that directly solve this problem, such as sum(), len(), or isinstance().
"""

def get_average(lst):
    total = 0
    count = 0
    
    for item in lst:
        if type(item) == int or type(item) == float:
            total += item
            count += 1
        elif type(item) == list:
            sub_total, sub_count = get_average(item)
            total += sub_total
            count += sub_count
        elif type(item) == dict:
            sub_total, sub_count = get_average(list(item.values()))
            total += sub_total
            count += sub_count
    
    if count == 0:
        return 0, 0
    
    return total, count

def average(lst):
    total, count = get_average(lst)
    return total / count