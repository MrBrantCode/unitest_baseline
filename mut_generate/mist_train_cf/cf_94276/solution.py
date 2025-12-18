"""
QUESTION:
Define a function `extract_substring` that takes three string arguments: `main_string`, `start_substring`, and `end_substring`. The function should return a string containing all the characters between the first occurrence of `start_substring` and the last occurrence of `end_substring` in `main_string`. If `start_substring` or `end_substring` does not exist in `main_string`, the function should return an empty string. The function should be case-sensitive and should not use any built-in functions or libraries specifically designed for this task.
"""

def extract_substring(main_string, start_substring, end_substring):
    # Find the index of the first occurrence of the start substring
    start_index = main_string.find(start_substring)
    
    # Find the index of the last occurrence of the end substring
    end_index = main_string.rfind(end_substring)
    
    # Check if either the start or end substring is not present in the main string
    if start_index == -1 or end_index == -1:
        return ""
    
    # Check if the start index is after the end index
    if start_index >= end_index:
        return ""
    
    # Extract the characters between the start and end substrings
    extracted_string = main_string[start_index + len(start_substring):end_index]
    return extracted_string