"""
QUESTION:
Create a function `credit_card_valid(card_number)` that takes a credit card number as input and returns `True` if the card number is valid according to the Luhn algorithm and `False` otherwise. The Luhn algorithm involves reversing the card number, doubling the value of every second digit, subtracting 9 if the doubled digit is greater than 9, and checking if the sum of all digits is divisible by 10.
"""

def credit_card_valid(card_number):
    # convert card number to a list of integers
    card_number = list(map(int, str(card_number)))
    # reverse the card number
    card_number.reverse()
    # double the value of every second digit
    for i in range(1, len(card_number), 2):
        card_number[i] = card_number[i] * 2
        if card_number[i] > 9:
            card_number[i] = card_number[i] - 9
    return sum(card_number) % 10 == 0