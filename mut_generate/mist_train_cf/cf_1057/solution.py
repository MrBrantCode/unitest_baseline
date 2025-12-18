"""
QUESTION:
Write a function called `extract_first_three` that takes a list as input and returns a list containing the first three unique elements from the input list. The function should not use the built-in slicing functionality and should have a time complexity of O(n), without using any additional data structures or libraries.
"""

def extract_first_three(lst):
    result = []
    count = 0
    for item in lst:
        if item not in result:
            result.append(item)
            count += 1
            if count == 3:
                break
    return result