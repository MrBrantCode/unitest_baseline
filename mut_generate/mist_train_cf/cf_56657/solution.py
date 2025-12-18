"""
QUESTION:
Write a function named `palindromic_substrings` that takes a string `strn` as input and returns a list of unique palindromic substrings and their count. The function should consider all possible substrings of the input string and identify the palindromic ones. The output should include the unique palindromic substrings and their total count. The time complexity of the solution should be provided.
"""

def palindromic_substrings(strn):
    """
    Returns a list of unique palindromic substrings and their count.

    Args:
    strn (str): The input string.

    Returns:
    list: A list of unique palindromic substrings.
    int: The count of unique palindromic substrings.
    """
    substrings = []
    for i in range(len(strn)):
        for j in range(i+1, len(strn)+1):
            sub = strn[i:j]
            if sub == sub[::-1]:
                substrings.append(sub)
    unique_substrings = list(set(substrings))
    return unique_substrings, len(unique_substrings)