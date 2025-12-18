"""
QUESTION:
Create a function named `extract_credit_card_numbers` that takes a string input and returns a list of valid credit card numbers in the format of 4 groups of 4 digits separated by dashes. The function should use a regular expression pattern to extract credit card numbers from the input string and then validate them using the Luhn algorithm.
"""

import re

def extract_credit_card_numbers(input_string):
    # create regular expression pattern
    pattern = r"\b\d{4}-\d{4}-\d{4}-\d{4}\b"
    
    # search for credit card numbers in the input string
    credit_card_numbers = re.findall(pattern, input_string)
    
    # validate the credit card numbers
    valid_credit_card_numbers = []
    for credit_card_number in credit_card_numbers:
        # remove dashes from the credit card number
        credit_card_number_digits = credit_card_number.replace("-", "")
        
        # validate the credit card number using Luhn algorithm
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
    
    # return the valid credit card numbers
    return valid_credit_card_numbers