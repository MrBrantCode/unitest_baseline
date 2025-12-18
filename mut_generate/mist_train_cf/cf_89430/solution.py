"""
QUESTION:
Write a function called `count_items` that takes a nested list as input and returns a dictionary where the keys are the items from the nested list and the values are the number of occurrences of each item. The function should have a time complexity of O(n), be implemented recursively, and be able to handle nested lists with any number of levels of nesting and different types of objects. The function should also be memory-efficient to handle extremely large nested lists.
"""

def count_items(nested_list):
    count_dict = {}
    def count_occurrences(nested_list):
        for item in nested_list:
            if isinstance(item, list):
                count_occurrences(item)
            else:
                count_dict[item] = count_dict.get(item, 0) + 1
    count_occurrences(nested_list)
    return count_dict