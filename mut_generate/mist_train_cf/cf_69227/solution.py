"""
QUESTION:
Implement two functions: `how_many_times` and `count_subsequences`. 

The function `how_many_times(string, substring)` should return a tuple containing the total count of occurrences of `substring` in `string` (including overlapping instances) and a list of their starting indices.

The function `count_subsequences(string, substring)` should return a tuple containing the total count of non-overlapping occurrences of `substring` in `string` and a list of their starting indices.

Both functions should take two parameters: `string` and `substring`, both of type `str`, and return a tuple of type `(int, [int])`.
"""

def how_many_times(string: str, substring: str) -> (int, [int]):
    """
    Returns a tuple containing the total count of occurrences of `substring` in `string` 
    (including overlapping instances) and a list of their starting indices.

    Args:
    string (str): The main string to search in.
    substring (str): The substring to search for.

    Returns:
    tuple: A tuple containing the total count of occurrences and a list of their starting indices.
    """
    tuple_of_occurences = (string.count(substring), [i for i in range(len(string)) if string.startswith(substring, i)]) 
    # Searching the string for the substring from every position
    return tuple_of_occurences 


def count_subsequences(string: str, substring: str) -> (int, [int]):
    """
    Returns a tuple containing the total count of non-overlapping occurrences of `substring` in `string` 
    and a list of their starting indices.

    Args:
    string (str): The main string to search in.
    substring (str): The substring to search for.

    Returns:
    tuple: A tuple containing the total count of non-overlapping occurrences and a list of their starting indices.
    """
    # Getting the starting indexes of the subsequences
    subsequence_indices = [i for i in range(len(string)) if string[i:].startswith(substring)]
    #getting subsequence count and indices by making sure they are not clashing
    subsequence_count = 0
    subsequence_positions = []
    
    for i in range(len(subsequence_indices)):
        if subsequence_indices[i] not in range(subsequence_indices[i-1], subsequence_indices[i-1]+len(substring)) if i>0 else True:
            subsequence_count += 1
            subsequence_positions.append(subsequence_indices[i])
    return (subsequence_count, subsequence_positions)