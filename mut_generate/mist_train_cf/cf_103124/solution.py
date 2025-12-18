"""
QUESTION:
Create a function `square_elements` that takes a list of integers as input and returns a new list containing the squares of each element. The function should use a for loop to iterate through the input list and have a time complexity of O(n) and space complexity of O(n). The input list can contain both positive and negative integers.
"""

def square_elements(input_list):
    result = []
    for num in input_list:
        result.append(num ** 2)
    return result