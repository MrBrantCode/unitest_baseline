"""
QUESTION:
Create a function `format_string` that takes a string as input and returns the formatted string. The function should capitalize the first letter of each word, replace all occurrences of the letter 'o' (case-insensitive) with the number '0', and append the string " - Updated!" to the end. The function should handle strings with multiple whitespace characters between words, and it should be case-insensitive when capitalizing the first letter of each word. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), where n is the length of the input string.
"""

def format_string(string):
    # Split the string into words using whitespace as the delimiter
    words = string.split()

    # Iterate through each word and capitalize the first letter
    for i in range(len(words)):
        words[i] = words[i].capitalize()

    # Join the capitalized words back into a single string
    formatted_string = ' '.join(words)

    # Replace all occurrences of 'o' with '0'
    formatted_string = formatted_string.replace('o', '0').replace('O', '0')

    # Append " - Updated!" to the end of the formatted string
    formatted_string += " - Updated!"

    return formatted_string