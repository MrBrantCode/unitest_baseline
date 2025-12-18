"""
QUESTION:
Define a function `extract_characters(main_string, start_substring, end_substring)` that extracts and returns a string containing all characters between the first occurrence of `start_substring` and the last occurrence of `end_substring` in `main_string`. The function should be case-sensitive and should not use any built-in functions or libraries specifically designed for this task. If either `start_substring` or `end_substring` does not exist in `main_string`, the function should return an empty string.
"""

def extract_characters(main_string, start_substring, end_substring):
    # Find the index of the first occurrence of the start substring
    start_index = main_string.find(start_substring)
    
    # Find the index of the last occurrence of the end substring
    end_index = main_string.rfind(end_substring)
    
    # If either start or end substring does not exist, return an empty string
    if start_index == -1 or end_index == -1:
        return ''
    
    # Return the characters between the start and end substrings
    return main_string[start_index + len(start_substring):end_index]