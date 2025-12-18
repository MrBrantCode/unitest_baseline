"""
QUESTION:
Create a function named `validate_credit_card_number` that takes a string representing a credit card number as input. The function should perform the following steps: 

- Check if the length of the input string is a valid credit card length (13, 15, or 16 digits). 
- Check if the first digit of the credit card number matches the accepted card type (4 for Visa, 5 for MasterCard, 6 for Discover). 
- Remove any non-digit characters from the input string. 
- Reverse the order of the digits in the resulting string. 
- Double the value of every second digit and subtract 9 from the result if it is greater than 9. 
- Add a checksum digit at the end of the credit card number, and revalidate the credit card number using the new checksum. 
- Sum all the digits obtained from step 5 together, and return True if the sum is divisible by 10, otherwise return False. 

Note: The function should be optimized to avoid unnecessary operations and improve performance.
"""

def validate_credit_card_number(card_number):
    # Check length of the input string
    if len(card_number) not in [13, 15, 16]:
        return False
    
    # Check first digit for accepted card type
    first_digit = int(card_number[0])
    if first_digit not in [4, 5, 6]:
        return False
    
    # Remove non-digit characters
    card_number = ''.join(filter(str.isdigit, card_number))
    
    # Reverse the order of the digits
    card_number = card_number[::-1]
    
    # Initialize checksum and flag
    checksum = 0
    is_second_digit = False
    
    # Double the value of every second digit, subtract 9 if greater than 9, and sum all the digits
    for digit in card_number:
        value = int(digit)
        if is_second_digit:
            value *= 2
            if value > 9:
                value -= 9
        checksum += value
        is_second_digit = not is_second_digit
    
    # Add the checksum digit needed to make the sum divisible by 10
    checksum += (10 - (checksum % 10)) % 10
    
    # Check if the sum is divisible by 10
    return (checksum % 10) == 0