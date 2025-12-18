"""
QUESTION:
Write a function named `substring_frequency` that takes two parameters: `input_string` and `length`. The function should determine the frequency of each repeated substring of the specified `length` within the `input_string`. The `length` can range from 2 to the length of the `input_string` divided by 2. The function should return a dictionary where the keys are the substrings and the values are their corresponding frequencies. The function should handle overlapping instances of substrings efficiently and be optimized to handle large strings.
"""

def substring_frequency(input_string, length):
    """
    This function determines the frequency of each repeated substring of the specified length within the input_string.
    
    Parameters:
    input_string (str): The string in which to find substrings.
    length (int): The length of the substrings to find.
    
    Returns:
    dict: A dictionary where the keys are the substrings and the values are their corresponding frequencies.
    """
    freqs = {}
    for i in range(0, len(input_string) - length + 1):
        substr = input_string[i:i + length]
        if substr in freqs:
            freqs[substr] += 1
        else:
            freqs[substr] = 1
    return freqs