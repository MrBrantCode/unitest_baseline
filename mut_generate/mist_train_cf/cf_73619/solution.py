"""
QUESTION:
Create a function `filter_elements(array, threshold)` that returns a subset of the input array. The function should only include elements with values less than the given threshold, and at least half of these elements must be even numbers. The input array contains integers and the threshold value is a positive integer.
"""

def filter_elements(array, threshold):
    # filter array for elements smaller than threshold
    filtered = [ele for ele in array if ele < threshold]

    # get count of even numbers in the filtered array
    even_count = len([ele for ele in filtered if ele % 2 == 0])

    # check if at least half of the elements in the filtered array are even
    if even_count >= len(filtered) / 2:
        return filtered
    else:
        # return an empty array if condition is not met
        return []