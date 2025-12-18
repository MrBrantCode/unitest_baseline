"""
QUESTION:
Create a function named `create_dictionary` that takes a list as input and returns a dictionary where each element in the input list is a key, and its corresponding value is a list of integers from 0 to the index of the key in the input list. The function should not take any other parameters besides the input list.
"""

def create_dictionary(lst):
    dictionary = {}
    for i in range(len(lst)):
        dictionary[lst[i]] = [j for j in range(i+1)]
    return dictionary