"""
QUESTION:
Write a function named `count_parameters` that takes a URL string as input and returns the total number of parameters present in the URL. The function should handle nested parameters and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the URL.
"""

def count_parameters(url):
    count = 0
    is_nested = False
    for char in url:
        if char == "?":
            count += 1
        elif char == "&":
            if not is_nested:
                count += 1
        elif char == "[":
            is_nested = True
        elif char == "]":
            if is_nested:
                count -= 1
                is_nested = False
    return count