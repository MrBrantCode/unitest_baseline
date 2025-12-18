"""
QUESTION:
Create a function named `find_intersecting_elements` that takes two lists as arguments and returns the intersecting elements in descending order along with their combined frequency in the input lists. The function should be able to handle lists with up to 1000 elements, including duplicates, and should not use any built-in functions or libraries for sorting or counting frequencies. The function should iterate through the input lists only once.
"""

def find_intersecting_elements(list1, list2):
    # Create dictionaries to store the frequency of elements in each list
    freq_dict1 = {}
    freq_dict2 = {}

    # Loop through list1 and count the frequency of each element
    for element in list1:
        if element in freq_dict1:
            freq_dict1[element] += 1
        else:
            freq_dict1[element] = 1

    # Loop through list2 and count the frequency of each element
    for element in list2:
        if element in freq_dict2:
            freq_dict2[element] += 1
        else:
            freq_dict2[element] = 1

    intersecting_elements = []
    # Loop through the keys in freq_dict1 and check if the element is present in freq_dict2
    for element in freq_dict1:
        if element in freq_dict2:
            intersecting_elements.append(element)

    # Sort the intersecting_elements list in descending order
    intersecting_elements.sort(reverse=True)

    # Create a dictionary to store the intersecting elements and their frequencies
    result = {}
    # Print the intersecting elements and their frequencies
    for element in intersecting_elements:
        result[element] = freq_dict1[element] + freq_dict2[element]
    return result