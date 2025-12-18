"""
QUESTION:
Find all unique values in a dataset of string and integer pairs, and return them in descending order of frequency. If two values have the same frequency, return them in ascending alphabetical order. If an error is detected in the dataset, return an empty list.

Implement a function named `get_unique_values(dataset)` that takes a list of lists as input, where each sublist contains a string and an integer, and returns a list of strings. 

Constraints:
- The length of the dataset will not exceed 10^6.
- The strings in the dataset will consist of lowercase letters only.
- The integers in the dataset will be positive integers less than or equal to 10^6.
- The final output list should not contain more than 10^6 elements.
- The dataset may contain errors, such as a string value in the integer field.
"""

def get_unique_values(dataset):
    """
    This function takes a list of lists as input where each sublist contains a string and an integer.
    It returns a list of strings representing unique values in descending order of frequency.
    If two values have the same frequency, they are returned in ascending alphabetical order.
    If an error is detected in the dataset, an empty list is returned.

    Args:
        dataset (list): A list of lists, where each sublist contains a string and an integer.

    Returns:
        list: A list of strings representing unique values.
    """

    # Initialize an empty dictionary to store the frequency of each value in the dataset
    freq_dict = {}

    # Iterate over each pair in the dataset
    for pair in dataset:
        # Check if the pair has exactly two elements and the second element is an integer
        if len(pair) != 2 or not isinstance(pair[1], int):
            # Return an empty list if the pair is invalid
            return []

        # Extract the value and frequency from the pair
        value = pair[0]
        frequency = pair[1]

        # Update the frequency of the value in the "freq_dict"
        freq_dict[value] = freq_dict.get(value, 0) + frequency

    # Sort the unique values based on their frequency and then alphabetically
    unique_values = sorted(freq_dict, key=lambda x: (-freq_dict[x], x))

    # Return the sorted list of unique values
    return unique_values