"""
QUESTION:
Write a function `extract_numbers_divisible_by_3` that takes a string as input, extracts all the numbers from the string that are divisible by 3, and returns them as a list.
"""

def extract_numbers_divisible_by_3(s):
    extracted_numbers = []
    current_number = ""
    
    for char in s:
        if char.isdigit():
            if current_number:
                current_number += char
            else:
                current_number = char
        else:
            if current_number:
                extracted_numbers.append(int(current_number))
                current_number = ""
    
    if current_number:
        extracted_numbers.append(int(current_number))
    
    return [num for num in extracted_numbers if num % 3 == 0]