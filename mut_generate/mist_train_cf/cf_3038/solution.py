"""
QUESTION:
Write a regular expression to match the pattern 'an example' in a string, given that it is preceded by the word 'This' and followed by a number enclosed in square brackets. The regular expression should match the number as well. Do not use lookaheads. The number can consist of one or more digits.
"""

def match_pattern(s):
    """
    Match the pattern 'an example' in a string, given that it is preceded by the word 'This' 
    and followed by a number enclosed in square brackets.

    Args:
        s (str): The input string.

    Returns:
        str: The matched number or None if the pattern is not found.
    """
    import re
    match = re.search(r'This is an example \[(\d+)\]', s)
    if match:
        return match.group(1)
    else:
        return None