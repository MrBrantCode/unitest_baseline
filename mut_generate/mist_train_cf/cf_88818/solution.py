"""
QUESTION:
Create a function named `find_intersecting_elements` that takes two lists of up to 1000 elements as input. The function should return the intersecting elements in descending order and calculate the frequency of each intersecting element in the input lists, handling cases where the input lists may contain duplicate elements. Implement the function using only one loop for counting the frequency of elements and without using any built-in functions or libraries for sorting or counting the frequency. The output should include each intersecting element and its total frequency in both lists.
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

    # Return a dictionary containing the intersecting elements and their frequencies
    return {element: freq_dict1[element] + freq_dict2[element] for element in intersecting_elements}