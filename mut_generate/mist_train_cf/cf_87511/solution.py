"""
QUESTION:
Create a function named `validate_credit_card` that takes a string of digits as input and returns the type of credit card the input string corresponds to. The function should support the following credit card types: 

- Visa cards starting with 4 and having a length of either 13 or 16 digits, with the sum of all digits being divisible by 10.
- Mastercard cards starting with 5 and having a length of 16 digits, with the sum of the squares of even-indexed digits equal to the sum of the cubes of odd-indexed digits.
- American Express cards starting with 3, followed by either 4 or 7, and having a length of 15 digits, with the card number being a palindrome.

If the input string does not match any of the criteria or contains non-numeric characters, the function should return "Invalid input". The function should not use any built-in credit card validation libraries or functions.
"""

def validate_credit_card(card_number):
    # Remove any whitespace characters from the card number
    card_number = card_number.replace(" ", "")

    # Check if the card number contains any non-numeric characters
    if not card_number.isdigit():
        return "Invalid input"

    # Check if the card number is a valid Visa card
    if card_number[0] == '4' and (len(card_number) == 13 or len(card_number) == 16) and sum(int(digit) for digit in card_number) % 10 == 0:
        return "Visa"

    # Check if the card number is a valid Mastercard
    if card_number[0] == '5' and len(card_number) == 16 and sum(int(digit)**2 for i, digit in enumerate(card_number) if i % 2 == 0) == sum(int(digit)**3 for i, digit in enumerate(card_number) if i % 2 != 0):
        return "Mastercard"

    # Check if the card number is a valid American Express card
    if (card_number[:2] == '34' or card_number[:2] == '37') and len(card_number) == 15 and card_number == card_number[::-1]:
        return "American Express"

    # Return "Invalid input" if the card number does not match any of the criteria
    return "Invalid input"