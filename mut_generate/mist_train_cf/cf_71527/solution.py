"""
QUESTION:
Create a function `find_pattern` that takes an array of two alphanumeric strings as input. The function should return a boolean indicating whether the second string (pattern) is present consecutively and in identical order within the first string, along with a list of tuples containing the start and end indices of each occurrence of the pattern in the first string. The function should have a time complexity efficient enough to handle large strings.
"""

def find_pattern(array):
    main_string = array[0]
    pattern = array[1]
    pattern_length = len(pattern)
    output = []
    result = False
    for i in range(len(main_string)):
        if main_string[i:i+pattern_length] == pattern:
            output.append((i, i+pattern_length-1))
            result = True
    return result, output