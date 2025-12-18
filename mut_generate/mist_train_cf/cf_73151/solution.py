"""
QUESTION:
Develop a function named `sanitize` that takes a nested list of integers as input. The function should remove all integers outside the range 0-9 from the list. The function should work recursively to handle nested lists of arbitrary depth.
"""

def sanitize(data):
    def is_arcane(num):
        return num < 0 or num > 9
    
    def traverse(data):
        for i in range(len(data)-1, -1, -1):
            if isinstance(data[i], list):
                traverse(data[i])
            elif isinstance(data[i], int) and is_arcane(data[i]):
                data.pop(i)

    traverse(data)
    return data