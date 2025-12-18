"""
QUESTION:
Write a function `find_max` that takes a list of numbers as input and returns the maximum number in the list without using built-in maximum functions. The list can contain negative numbers and decimals. If the input is not a valid non-empty list, return an error message.
"""

def find_max(list_input):
    if (type(list_input) == list) and len(list_input) > 0: 
        max_number = list_input[0]  

        for number in list_input:  
            if number > max_number:  
                max_number = number  

        return max_number  

    else:
        return 'Invalid list provided'  