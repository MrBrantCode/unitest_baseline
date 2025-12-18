"""
QUESTION:
Implement a function `find_most_frequent(lst)` that finds the most frequent element(s) in a list. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(k), where k is the number of unique elements in the list. The function should be able to handle lists with elements of any data type and return all elements with the highest frequency if there are multiple.
"""

def find_most_frequent(lst):
    counts = {}
    max_freq = 0
    max_elements = []

    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

        if counts[element] > max_freq:
            max_freq = counts[element]
            max_elements = [element]
        elif counts[element] == max_freq:
            max_elements.append(element)

    return max_elements