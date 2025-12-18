"""
QUESTION:
Implement the function `validateCreditCard` that takes a credit card number string in the format "XXXX-XXXX-XXXX-XXXX" as input and returns a boolean value indicating whether the credit card number is potentially valid. The validation rules are as follows: the credit card number must consist of 16 digits, the first digit must be a 4, and each group of 4 digits separated by hyphens must not contain any repeating digits consecutively.
"""

def validate_credit_card(credit_card_number):
    # Rule 1: Check if the credit card number consists of 16 digits in the format "XXXX-XXXX-XXXX-XXXX"
    if len(credit_card_number) != 19 or not credit_card_number.replace("-", "").isdigit():
        return False
    
    # Rule 2: Check if the first digit of the credit card number is 4
    if credit_card_number[0] != '4':
        return False
    
    # Rule 3: Check for consecutive repeating digits in each group of 4 digits
    groups = credit_card_number.split("-")
    for group in groups:
        for i in range(len(group) - 1):
            if group[i] == group[i + 1]:
                return False
    
    return True