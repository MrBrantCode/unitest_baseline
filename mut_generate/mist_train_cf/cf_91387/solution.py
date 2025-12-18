"""
QUESTION:
Extract all numbers from a given string and return them as a list. The numbers in the string may be single or multiple digits and can be embedded in the string. Implement a function named 'extract_numbers' that takes a string as input and returns a list of integers. The function should not use regular expressions.
"""

def extract_numbers(string):
    numbers = []
    current_number = ''
    
    for i in range(len(string)):
        if string[i].isdigit():
            current_number += string[i]
            
            # Check if the next character is also a digit
            if i < len(string) - 1 and string[i+1].isdigit():
                continue
            
            numbers.append(int(current_number))
            current_number = ''
    
    return numbers