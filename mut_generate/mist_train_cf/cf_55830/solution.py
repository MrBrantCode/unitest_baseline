"""
QUESTION:
Write a function called `replace_third_occurrences` that takes a string as input. This function should replace every third occurrence of the character 'a' (regardless of case) in the string with '#'.
"""

def replace_third_occurrences(input_string):
    count = 0
    output_string = ""
    
    for char in input_string:
        if char.lower() == 'a':
            count += 1
            if count % 3 == 0:
                output_string += '#'
            else:
                output_string += char
        else:
            output_string += char
            
    return output_string