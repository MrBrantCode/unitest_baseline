"""
QUESTION:
Recognize the type of a credit card from a given string of numbers. The function should identify the credit card type based on the starting digits. 

The function should be named `recognize_credit_card` and take one parameter `card_number`. 

It should return the type of the credit card ("Visa", "Mastercard", "American Express", "Discover", or "Unknown") if the input string is valid. If the input string contains any non-numeric characters (excluding spaces), the function should return "Invalid input".
"""

def recognize_credit_card(card_number):
    card_number = card_number.replace(" ", "")  # Remove any spaces
    
    if not card_number.isnumeric():  # Check for non-numeric characters
        return "Invalid input"
    
    first_digit = card_number[0]
    
    if first_digit == '4':
        return "Visa"
    elif first_digit == '5':
        return "Mastercard"
    elif first_digit == '3':
        if card_number[1] == '4' or card_number[1] == '7':
            return "American Express"
    elif first_digit == '6':
        if card_number.startswith('6011'):
            return "Discover"
    
    return "Unknown"