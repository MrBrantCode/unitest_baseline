"""
QUESTION:
Extract the country code from a given phone number string. The country code is a two-digit number that appears after the '+' character and may be followed by spaces or dashes. The phone number may contain additional spaces or dashes. The function should return the country code as a string. The time complexity should be O(n), where n is the length of the input string. If the country code is not found, return None.
"""

def extract_country_code(phone_number):
    country_code = ''
    digits_count = 0
    
    for char in phone_number:
        if char == '+':
            continue
        
        if char.isdigit():
            country_code += char
            digits_count += 1
            
            if digits_count == 2:
                return country_code
    
    return None  # Return None if country code is not found