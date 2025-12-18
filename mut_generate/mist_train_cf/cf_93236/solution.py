"""
QUESTION:
Write a function `count_distinct_elements` that takes a list of numbers as input and returns the number of distinct elements in the list. The function should not use any built-in Python functions or libraries that directly solve the problem, and it should have a time complexity of O(n), where n is the length of the list.
"""

def count_distinct_elements(numbers_list):
    distinct_elements = {}
    count = 0
    for num in numbers_list:
        if num not in distinct_elements:
            distinct_elements[num] = True
            count += 1
    return count