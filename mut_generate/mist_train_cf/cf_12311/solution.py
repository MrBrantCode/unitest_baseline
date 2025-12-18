"""
QUESTION:
Write a function called `format_strings` that takes a list of strings as input. The function should return a new list where the first letter of each word in each string is in upper case and all other characters are in lower case. The function should have a time complexity of O(n), where n is the total number of characters in all strings, and a space complexity of O(1), excluding the space needed for the output.
"""

def format_strings(strings):
    formatted_strings = []
    for string in strings:
        formatted_string = ""
        capitalize_next = True
        for char in string:
            if capitalize_next and char.isalpha():
                formatted_string += char.upper()
                capitalize_next = False
            else:
                formatted_string += char.lower()
                if char == " ":
                    capitalize_next = True
        formatted_strings.append(formatted_string)
    return formatted_strings