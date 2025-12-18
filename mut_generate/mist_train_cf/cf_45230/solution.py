"""
QUESTION:
Write a function named `count_and_remove_duplicates` that takes a list as input, removes repeated elements while maintaining their original order, and returns the modified list along with a dictionary containing the counts of repeated elements. The dictionary should only include elements that appear more than once in the original list. Implement the function without using built-in functions or methods for counting elements in a list.
"""

def count_and_remove_duplicates(elements_list):
    element_counts = {}
    new_list = []
    for element in elements_list:
        if element not in element_counts:
            element_counts[element] = 1 # first occurance of element
            new_list.append(element) # add it to new list
        else:
            element_counts[element] += 1 # add count for the element
    # Filter out elements with count 1 from the dictionary
    element_counts = {element: count for element, count in element_counts.items() if count > 1}
    return new_list, element_counts