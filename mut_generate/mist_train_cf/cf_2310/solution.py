"""
QUESTION:
Write a function named `extract_numbers` that takes a string as input, extracts all numbers divisible by 3 from the string, and returns them as a list. The input string may contain multiple numbers and non-numeric characters. The time complexity should be O(n), where n is the length of the string, and the space complexity should be O(m), where m is the number of numbers divisible by 3 in the string.
"""

def extract_numbers(string):
    extracted_numbers = []
    current_number = ""

    for char in string:
        if char.isdigit():
            current_number += char
        elif current_number:
            if int(current_number) % 3 == 0:
                extracted_numbers.append(int(current_number))
            current_number = ""

    if current_number and int(current_number) % 3 == 0:
        extracted_numbers.append(int(current_number))

    return extracted_numbers