"""
QUESTION:
Remove duplicates from a list of integers while preserving the order of the remaining elements. 

The input list contains integers between -10^9 and 10^9. Implement a function `remove_duplicates(my_list)` that takes the input list as a parameter. The algorithm should have a time complexity of O(n) and use O(n) additional space.
"""

def remove_duplicates(my_list):
    unique_elements = set()
    result = []
    for num in my_list:
        if num not in unique_elements:
            unique_elements.add(num)
            result.append(num)
    return result