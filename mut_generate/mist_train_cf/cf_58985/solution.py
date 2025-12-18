"""
QUESTION:
Write a function `sort_string(string)` that takes a string as input, converts it to lower case, and rearranges its characters alphabetically. If the input is not a string or any error occurs during execution, the function should return a descriptive error message.
"""

def sort_string(s):
    try:
        lower_case_string = s.lower()
        sorted_string = ''.join(sorted(lower_case_string))
        return sorted_string
    except Exception as e:
        return f"An error occurred: {str(e)}"