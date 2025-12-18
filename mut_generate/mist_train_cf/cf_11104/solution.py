"""
QUESTION:
Write a function called `validate_credit_card_number` that takes a string representing a credit card number as input and returns a boolean value indicating whether the number is valid or not. The function should validate the credit card number according to the Luhn algorithm, which involves removing non-digit characters, reversing the order of the digits, doubling every second digit, subtracting 9 from doubled digits greater than 9, summing all the digits, and checking if the sum is divisible by 10.
"""

def validate_credit_card_number(card_number):
    # Step 1: Remove non-digit characters
    card_number = ''.join(filter(str.isdigit, card_number))
    
    # Step 2: Reverse the order of the digits
    card_number = card_number[::-1]
    
    # Step 3: Double the value of every second digit
    doubled_digits = [int(digit) * 2 if i % 2 == 1 else int(digit) for i, digit in enumerate(card_number)]
    
    # Step 4: Subtract 9 from doubled digits greater than 9
    subtracted_digits = [digit - 9 if digit > 9 else digit for digit in doubled_digits]
    
    # Step 5: Sum all the digits
    digit_sum = sum(subtracted_digits)
    
    # Step 6: Check if sum is divisible by 10
    return digit_sum % 10 == 0