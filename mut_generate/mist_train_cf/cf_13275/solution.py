"""
QUESTION:
Write a function `count_parameters` to count the number of parameters present in a given URL string. The function should handle URLs with nested parameters, such as arrays or objects. It should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the URL. The function should return the total number of parameters in the URL.
"""

def count_parameters(url):
    count = 0
    nested_level = 0
    for char in url:
        if char == '&' and nested_level == 0:
            count += 1
        elif char == '[' or char == '{':
            nested_level += 1
        elif char == ']' or char == '}':
            nested_level -= 1
    return count + 1  # Add 1 for the last parameter