"""
QUESTION:
Implement a function `find_and_replace(string, keyword, replacement)` that takes a string and two keywords as input. The function should count the occurrences of the `keyword` in the `string`, replace the first occurrence of the `keyword` with the `replacement`, and return a tuple containing the count and the modified string. The function should not use Python's built-in string search and replace methods.
"""

def find_and_replace(string, keyword, replacement):
    # Find the length of the keyword
    keyword_length = len(keyword)
    # Initialize the count variable and index of first occurrence
    count, first_index = 0, None
    # Loop to find the keyword in the string
    for i in range(len(string) - keyword_length + 1):
        if string[i:i+keyword_length] == keyword:
            count += 1
            if first_index is None:
                first_index = i
    # Create a resulting string
    result_string = string
    # If keyword was found in the string,
    # replace first occurrence of it using slicing and concatenation
    if first_index is not None:
        result_string = string[:first_index] + replacement + string[first_index + keyword_length:]
    # Return the count and the string with the keyword replaced
    return count, result_string