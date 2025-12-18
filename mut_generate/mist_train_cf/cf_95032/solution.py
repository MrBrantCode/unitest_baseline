"""
QUESTION:
Write a function `find_most_frequent` that finds the most frequent elements in a given list. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(k), where k is the number of unique elements in the list. The function should return all elements with the highest frequency and be able to handle lists with elements of any data type.
"""

def find_most_frequent(lst):
    counts = {}
    max_freq = 0
    max_elements = []

    # Count the frequency of each element
    for element in lst:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1

        # Update max_freq and max_elements if necessary
        if counts[element] > max_freq:
            max_freq = counts[element]
            max_elements = [element]
        elif counts[element] == max_freq:
            max_elements.append(element)

    return max_elements