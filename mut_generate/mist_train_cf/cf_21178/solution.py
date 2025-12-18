"""
QUESTION:
Create a function called `remove_duplicates` that takes a list of strings as an argument. It should return a list containing only non-duplicate strings while maintaining the order of their appearance in the input list. The function must have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates(strings):
    seen = set()
    result = []
    
    for string in strings:
        if string not in seen:
            seen.add(string)
            result.append(string)
    
    return result