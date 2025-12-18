"""
QUESTION:
Write a function `detectDupes` that takes a tuple `t` as input, where `t` contains only integers and strings. The function should return a dictionary where each key is a unique element from `t` and each value is the 'weight' of that element, calculated as follows:

*   If the element is an integer, its weight is 3 times its count in `t`.
*   If the element is a string, its weight is 5 times its count in `t`.

The function should ignore any elements in `t` that are not integers or strings, and it should only include elements in the output dictionary if they appear more than once in `t`.
"""

def detectDupes(t):
    """
    This function calculates the weight of each unique element in the input tuple.
    The weight of an integer is 3 times its count, and the weight of a string is 5 times its count.
    It only includes elements that appear more than once in the tuple and ignores other types.

    Args:
    t (tuple): A tuple containing integers and strings.

    Returns:
    dict: A dictionary where each key is a unique element from the tuple and each value is its weight.
    """

    # Define valid types and their corresponding weights
    valid_types = (int, str)
    type_weights = {int: 3, str: 5}

    # Initialize an empty dictionary to store the count of each element
    count_dict = {}

    # Iterate over each element in the tuple
    for item in t:
        # Check if the element is of a valid type
        if isinstance(item, valid_types):
            # Increment the count of the element in the dictionary
            count_dict[item] = count_dict.get(item, 0) + 1

    # Initialize an empty dictionary to store the result
    result = {}

    # Iterate over each element and its count in the count dictionary
    for item, count in count_dict.items():
        # Check if the element appears more than once in the tuple
        if count > 1:
            # Calculate the weight of the element and add it to the result dictionary
            result[item] = count * type_weights[type(item)]

    return result