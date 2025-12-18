"""
QUESTION:
Write a Python function `validate(card_num)` that checks if a given credit card number `card_num` is valid. The function should return "Valid" if the card number is valid, and "Invalid" otherwise. 

A valid credit card number consists of exactly 16 digits, starts with 4, 5, or 6, contains no alphabets or special characters, and does not have four or more consecutive repeated digits. Additionally, the card number must pass a simplified version of the Luhn Algorithm check. 

The Luhn Algorithm works by doubling every second digit from the right, adding the digits of the resulting numbers if they are two digits, and checking if the total sum is a multiple of 10.
"""

def validate(card_num):
    if not card_num.isdigit() or len(card_num) != 16:
        return "Invalid"       
    if card_num[0] not in ['4', '5', '6']:
        return "Invalid"       
    for i in range(len(card_num) - 3):
        if card_num[i] == card_num[i + 1] == card_num[i + 2] == card_num[i + 3]:
            return "Invalid"       
    num_arr = [int(x) for x in card_num]
    reverse_num_arr = num_arr[::-1]
    for i in range(len(reverse_num_arr)):
        if i % 2 != 0:
            reverse_num_arr[i] = reverse_num_arr[i] * 2
            if reverse_num_arr[i] > 9:
                reverse_num_arr[i] = int(reverse_num_arr[i] / 10) + reverse_num_arr[i] % 10
    if sum(reverse_num_arr) % 10 != 0:
        return "Invalid"       
    return "Valid"