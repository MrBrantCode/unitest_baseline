"""
QUESTION:
Create a function named `extract_credit_card_numbers` that takes a string input and returns a list of valid credit card numbers. The function must use a regular expression pattern to match credit card numbers in the format of 4 groups of 4 digits separated by dashes, and validate the extracted numbers using the Luhn algorithm.
"""

import re

def extract_credit_card_numbers(input_string):
    pattern = r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
    credit_card_numbers = re.findall(pattern, input_string)
    valid_credit_card_numbers = []
    
    for credit_card_number in credit_card_numbers:
        credit_card_number_digits = credit_card_number.replace("-", "")
        sum = 0
        num_digits = len(credit_card_number_digits)
        oddeven = num_digits & 1
        
        for count in range(0, num_digits):
            digit = int(credit_card_number_digits[count])
            
            if not (( count & 1 ) ^ oddeven ):
                digit = digit * 2
                
            if digit > 9:
                digit = digit - 9
                
            sum = sum + digit
            
        if (sum % 10) == 0:
            valid_credit_card_numbers.append(credit_card_number)
    
    return valid_credit_card_numbers