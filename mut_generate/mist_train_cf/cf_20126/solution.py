"""
QUESTION:
Create a function `create_sorted_count_dict` that takes a list of elements as input and returns a dictionary where the keys are the unique elements from the list and the values are their respective counts. The dictionary should not include elements with a count of 0 and should be sorted in descending order based on the counts of the elements.
"""

def create_sorted_count_dict(lst):
    """
    This function takes a list of elements as input and returns a dictionary 
    where the keys are the unique elements from the list and the values are their 
    respective counts. The dictionary does not include elements with a count of 0 
    and is sorted in descending order based on the counts of the elements.

    Args:
        lst (list): A list of elements.

    Returns:
        dict: A dictionary with unique elements as keys and their counts as values.
    """
    # Create a dictionary to store the unique elements and their counts
    dictionary = {}
    
    # Iterate through the list
    for element in lst:
        # If the element is already in the dictionary, increment its count
        if element in dictionary:
            dictionary[element] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            dictionary[element] = 1
    
    # Remove elements with count 0 from the dictionary
    dictionary = {key: value for key, value in dictionary.items() if value != 0}
    
    # Sort the dictionary in descending order based on the counts of the elements
    dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
    
    return dictionary