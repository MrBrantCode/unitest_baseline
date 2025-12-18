"""
QUESTION:
Create a function named `remove_and_count` that takes a list as input and returns two outputs. The function should remove all repeated elements from the list while maintaining the original order of the remaining elements, and count the frequency of each element initially present. The first output should be the new list with duplicates removed, and the second output should be a dictionary showing the initial count of each element in the original list. You cannot use built-in Python functionalities for counting frequency and removing duplicates.
"""

def remove_and_count(elements_list):
    frequencies = {}
    new_elements = []
    for element in elements_list:
        if element not in frequencies:
            frequencies[element] = 1
            new_elements.append(element)
        else:
            frequencies[element] += 1
    return new_elements, frequencies