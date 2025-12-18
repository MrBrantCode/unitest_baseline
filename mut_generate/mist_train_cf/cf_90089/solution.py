"""
QUESTION:
Implement a function `remove_duplicates` that takes a list of elements as input and returns a new list containing the unique elements from the input list in the same order as they appeared in the original list. The function should not use any built-in functions or data structures that could potentially solve the problem, such as sets or dictionaries. The function should have a time complexity of O(n^2) and use O(n) additional space. The function should be able to handle lists containing a mix of integers, strings, and negative floating-point numbers.
"""

def remove_duplicates(my_list):
    unique_list = []
    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list