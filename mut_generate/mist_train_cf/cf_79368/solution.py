"""
QUESTION:
Implement a function `remove_and_count_not_only` that takes an array of strings as input, removes any occurrences of the phrase "not only" from the strings, and returns the modified array, the total number of occurrences of the phrase "not only", and the total number of characters removed. The function should handle special characters and count the characters removed including the phrase "not only".
"""

def remove_and_count_not_only(arr):
    """
    This function removes any occurrences of the phrase "not only" from the strings in the input array, 
    and returns the modified array, the total number of occurrences of the phrase "not only", 
    and the total number of characters removed.

    Args:
        arr (list): A list of strings.

    Returns:
        tuple: A tuple containing the modified array, the total number of occurrences of "not only", 
        and the total number of characters removed.
    """
    phrase = "not only"
    num_occurrences = sum(s.count(phrase) for s in arr)
    total_chars_removed = num_occurrences * len(phrase)
    modified_arr = [s.replace(phrase, '') for s in arr]
    return modified_arr, num_occurrences, total_chars_removed