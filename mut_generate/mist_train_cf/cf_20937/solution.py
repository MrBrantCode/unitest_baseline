"""
QUESTION:
Write a function `count_parameters(url)` that takes a URL as input and returns the number of parameters present in the URL. The function should handle URLs with nested parameters and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the URL. The input URL can have multiple levels of nested parameters, including arrays or objects.
"""

def count_parameters(url):
    count = 0
    nestedCount = 0
    
    for char in url:
        if char == '?':
            nestedCount += 1
        elif char == '&' and nestedCount > 0:
            count += 1
        elif char == '[':
            nestedCount += 1
        elif char == ']' and nestedCount > 0:
            nestedCount -= 1
        elif char == '=' and nestedCount > 0:
            count += 1
            
    return count