"""
QUESTION:
Create a function called `check_and_count` that takes two parameters: an array and an element. The function should traverse the array only once and return the count of the given element's occurrences in the array. The function should have a time complexity of O(n), where n is the total number of elements in the array.
"""

def check_and_count(array, element):
    count = 0
    for i in array:
        if i == element:
            count += 1
    return count