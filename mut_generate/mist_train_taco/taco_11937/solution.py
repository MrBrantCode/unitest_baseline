"""
QUESTION:
# Covfefe


Your are given a string. You must replace the word(s) `coverage` by `covfefe`, however, if you don't find the word `coverage` in the string, you must add `covfefe` at the end of the string with a leading space.

For the languages where the string is not immutable (such as ruby), don't modify the given string, otherwise this will break the test cases.
"""

def replace_or_append_covfefe(input_string: str) -> str:
    """
    Replaces the word 'coverage' with 'covfefe' in the input string.
    If 'coverage' is not found, appends ' covfefe' to the end of the string.

    :param input_string: The input string to be processed.
    :return: The modified string.
    """
    if 'coverage' in input_string:
        return input_string.replace('coverage', 'covfefe')
    else:
        return input_string + ' covfefe'