"""
QUESTION:
Implement a function `find_second_most_common_element` that takes a list of elements as input and returns the second most frequently occurring element in the list. The function should have a time complexity of O(n), where n is the length of the list, and it should only consider elements that appear at least twice in the list. If there is no second most common element, the function can return any value (e.g., None).
"""

def find_second_most_common_element(lst):
    count_dict = {}
    for elem in lst:
        count_dict[elem] = count_dict.get(elem, 0) + 1
    
    max_count = -1
    second_max_count = -1
    for count in count_dict.values():
        if count > max_count:
            second_max_count = max_count
            max_count = count
        elif count > second_max_count and count < max_count:
            second_max_count = count
    
    for elem, count in count_dict.items():
        if count == second_max_count:
            return elem