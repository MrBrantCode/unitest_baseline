"""
QUESTION:
Design a function named `vowel_frequency` that accepts a string `input_string` and two integers `n` and `m` as parameters. The function should calculate the total number of vowels in the string and return a frequency table detailing the quantity of each vowel present in the string, with the following restrictions: the length of `input_string` cannot exceed `n` characters and the total number of vowels cannot exceed `m`.
"""

def vowel_frequency(input_string, n, m):
    """
    Calculate the total number of vowels in the string and return a frequency table detailing the quantity of each vowel present in the string.

    Parameters:
    input_string (str): The input string to be processed.
    n (int): The maximum allowed length of the input string.
    m (int): The maximum allowed number of vowels in the input string.

    Returns:
    dict or str: A dictionary containing the frequency of each vowel if the string is valid, otherwise an error message.
    """

    if len(input_string) > n:
        return "Error: the length of the string exceeds the limit"
    
    vowels = "aeiou"
    count = {i: 0 for i in vowels}
    total_vowels = 0
    
    for char in input_string.lower():
        if char in vowels:
            count[char] += 1
            total_vowels += 1
    
    if total_vowels > m:
        return "Error: the number of vowels in the string exceeds the limit"
    else:
        return {"total_vowels": total_vowels, "frequency_table": {key: value for key, value in count.items() if value != 0}}