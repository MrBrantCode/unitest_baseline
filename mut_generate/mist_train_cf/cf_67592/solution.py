"""
QUESTION:
Create a function `string_manipulator` that takes two parameters: an input string and an operation. The function should perform different string manipulation operations based on the operation parameter. The operations should include reversing the string, converting to uppercase, converting to lowercase, and replacing vowels. If the operation does not match any existing case, the function should return a meaningful error message.
"""

def string_manipulator(input_string, operation):
    def reverse_string(input_string):
        return input_string[::-1]

    def uppercase_string(input_string):
        return input_string.upper()

    def lowercase_string(input_string):
        return input_string.lower()

    def replace_vowels(input_string):
        vowels = ('a', 'e', 'i', 'o', 'u') 
        return ''.join('_' if char.lower() in vowels else char for char in input_string)

    strings_operations = {
        'reverse': reverse_string,
        'upper': uppercase_string,
        'lower': lowercase_string,
        'replace_vowels': replace_vowels
    }

    try:
        return strings_operations[operation](input_string)
    except KeyError:
        return f"Unfortunately, we do not support this kind of operation ('{operation}')"