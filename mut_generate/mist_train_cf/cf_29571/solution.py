"""
QUESTION:
Implement a function `format_phone_number` that takes a string as input and returns a string in the standard phone number format. The standard phone number format consists of three groups of numbers separated by hyphens, where the first group contains 3 digits, the second group contains 3 digits, and the third group contains 4 digits. The input string may contain non-numeric characters, which should be removed. If the input string does not contain exactly 10 digits, the function should return "Invalid phone number".
"""

def format_phone_number(input_string: str) -> str:
    digits = ''.join(filter(str.isdigit, input_string))  # Extract only the digits from the input string
    if len(digits) == 10:  # Check if the extracted digits form a complete phone number
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"  # Format the digits into a standard phone number format
    else:
        return "Invalid phone number"