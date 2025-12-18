"""
QUESTION:
Write a function named `explode_and_sort` that takes a string as input and a delimiter. The function should split the string into a list using the delimiter, remove any leading or trailing whitespace from each element, remove any duplicate elements, and return the resulting list in alphabetical order. The input string may contain duplicate elements and may have whitespace characters before and after the delimiter.
"""

def explode_and_sort(input_str, delimiter):
    """
    Splits a string into a list using a delimiter, removes duplicates, 
    trims whitespace from each element, and returns the list in alphabetical order.

    Args:
        input_str (str): The input string to be processed.
        delimiter (str): The delimiter to split the string.

    Returns:
        list: A list of unique elements in alphabetical order.
    """
    # remove whitespace characters before and after each element
    trimmed_str = input_str.strip()
    
    # explode the string with the given delimiter
    exploded_list = trimmed_str.split(delimiter)
    
    # remove leading/trailing whitespace from each element
    trimmed_list = [item.strip() for item in exploded_list]
    
    # remove duplicate elements
    unique_list = list(set(trimmed_list))
    
    # sort the list in alphabetical order
    sorted_list = sorted(unique_list)
    
    return sorted_list