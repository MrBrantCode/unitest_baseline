"""
QUESTION:
Write a function named `extract_first_three` that takes a list as input and returns a new list containing the first three unique elements of the input list. Do not use built-in slicing or any additional data structures/libraries, and ensure a time complexity of O(n).
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