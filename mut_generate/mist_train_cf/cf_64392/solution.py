"""
QUESTION:
Write a function called `lowercase_except_4th_multiple_of_5` that takes an input string and returns the string with all characters in lowercase, except for those at every 4th index (1-indexed) if the length of the input string is a multiple of 5. If the length of the string is not a multiple of 5, the function should return the string with all characters in lowercase.
"""

def lowercase_except_4th_multiple_of_5(input_string):
    if len(input_string) % 5 != 0:
        return input_string.lower() 

    output_string = ""
    for i in range(len(input_string)):
        if (i+1) % 4 != 0:
            output_string += input_string[i].lower()
        else:
            output_string += input_string[i]
    
    return output_string