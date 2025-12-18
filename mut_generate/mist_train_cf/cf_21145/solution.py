"""
QUESTION:
Create a function named `longest_strings` that takes an array of strings as input. The function should return a new array containing all the strings from the input array with the maximum length. The function should handle empty input arrays and arrays containing only empty strings. The input array will not contain more than 1000 strings and each string will not exceed 1000 characters in length.
"""

def longest_strings(arr):
    # If input array is empty, return an empty array
    if len(arr) == 0:
        return []
    
    # Initialize the longest length to 0
    longest_length = 0
    
    # Iterate through each string in the input array
    for string in arr:
        # Update the longest length if the current string has a longer length
        longest_length = max(longest_length, len(string))
    
    # Initialize an empty array to store the longest strings
    longest_strings_arr = []
    
    # Iterate through each string in the input array again
    for string in arr:
        # If the length of the current string is equal to the longest length, add it to the longest strings array
        if len(string) == longest_length:
            longest_strings_arr.append(string)
    
    return longest_strings_arr