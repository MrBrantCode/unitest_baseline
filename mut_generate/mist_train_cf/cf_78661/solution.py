"""
QUESTION:
Write a function `regex_complexity` to explain the time complexity of regular expression matching in various programming languages, particularly in Python, Java, and Perl, for both backtracking and Thompson's NFA algorithms. Describe the time complexity of regex substitution.
"""

def regex_complexity(pattern_length, string_length):
    """
    Calculate the time complexity of regular expression matching.

    Args:
    pattern_length (int): The length of the regex pattern.
    string_length (int): The length of the string.

    Returns:
    str: A string describing the time complexity of the regex matching.
    """

    # Backtracking algorithm complexity
    backtracking_complexity = f"O(2^{string_length})"  # worst-case

    # Thompson's NFA algorithm complexity
    thompson_complexity = f"O({pattern_length}*{string_length})"

    # Substitution complexity
    substitution_complexity = f"O({pattern_length}*{string_length} + {string_length})"

    return backtracking_complexity, thompson_complexity, substitution_complexity