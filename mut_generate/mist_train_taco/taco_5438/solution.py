"""
QUESTION:
Write function toAcronym which takes a string and make an acronym of it.

Rule of making acronym in this kata:

1. split string to words by space char
2. take every first letter from word in given string
3. uppercase it
4. join them toghether



Eg:


Code wars -> C, w -> C W -> CW
"""

def to_acronym(input_string: str) -> str:
    """
    Generate an acronym from the given input string.

    Parameters:
    input_string (str): The input string from which the acronym will be generated.

    Returns:
    str: The acronym generated from the input string.
    """
    return ''.join((word[0] for word in input_string.split())).upper()