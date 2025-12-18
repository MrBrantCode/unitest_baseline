"""
QUESTION:
Create a function called `format_string` that takes a string as input, capitalizes the first letter of each word in a case-insensitive manner, replaces all occurrences of 'o' with '0', and appends " - Updated!" to the end of the string. The function should be able to handle strings with multiple whitespace characters between words. The time complexity of the function should be O(n), where n is the length of the input string, and the space complexity should be O(1).
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
    formatted_string = formatted_string.replace('o', '0')

    # Append " - Updated!" to the end of the formatted string
    formatted_string += " - Updated!"

    return formatted_string