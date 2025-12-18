"""
QUESTION:
Write a function `analyze_strings` that takes a list of strings as input. The function should calculate the combined length of all strings in the list that do not contain the letter 'a', and return this value along with the total number of strings in the list that have a length greater than or equal to 5. Additionally, the function should keep track of the indices of the strings that contain the letter 's' and calculate their average length.
"""

def analyze_strings(strings):
    """
    Analyze a list of strings.

    Args:
    strings (list): A list of strings.

    Returns:
    tuple: A tuple containing the combined length of all strings without 'a',
           the total number of strings with length greater than or equal to 5,
           the indices of strings containing 's', and the average length of strings containing 's'.
    """
    combined_length = 0
    strings_greater_than_5 = 0
    indices_of_s = []
    length_of_s_strings = 0

    for index, string in enumerate(strings):
        if 'a' not in string:
            combined_length += len(string)
            if len(string) >= 5:
                strings_greater_than_5 += 1
        if 's' in string:
            indices_of_s.append(index)
            length_of_s_strings += len(string)

    if indices_of_s:
        average_length_of_s_strings = length_of_s_strings / len(indices_of_s)
    else:
        average_length_of_s_strings = 0

    return combined_length, strings_greater_than_5, indices_of_s, average_length_of_s_strings