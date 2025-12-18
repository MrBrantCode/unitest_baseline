"""
QUESTION:
Write a function called `find_common_elements` that finds the most common element(s) in a given list of strings. The function should not use any built-in functions like `count` or `max`. If multiple elements share the highest frequency, return all of them.
"""

def find_common_elements(mylist):
    frequency_dict = {}
    for element in mylist:
        if element not in frequency_dict:
            frequency_dict[element] = 1
        else:
            frequency_dict[element] += 1
    max_frequency = 0
    max_frequency_elements = []
    for element, frequency in frequency_dict.items():
        if frequency > max_frequency:
            max_frequency = frequency
            max_frequency_elements = [element]
        elif frequency == max_frequency:
            max_frequency_elements.append(element)
    return max_frequency_elements