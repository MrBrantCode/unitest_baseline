"""
QUESTION:
Implement a function called `count_edits` that takes three parameters: `original` and `target`, both of which are strings of the same length, and `window`, an integer representing the size of the sliding window. The function should calculate the total number of edits required to transform the substrings within the sliding window in the `original` string into the corresponding substrings in the `target` string. The function should return the total number of edits required.
"""

def count_edits(original: str, target: str, window: int) -> int:
    if len(original) != len(target):
        return -1  # Strings must be of equal length for comparison

    edits = 0
    for i in range(len(original) - window + 1):
        substring = original[i:i + window]
        target_substring = target[i:i + window]
        edits += sum(1 for char1, char2 in zip(substring, target_substring) if char1 != char2)

    return edits