"""
QUESTION:
Create a function named `complex_digit_count` that takes an integer as input. The function should return a tuple of three values representing the count of even digits, odd digits, and digits divisible by 3 within the input integer. The function should ignore the sign of the input integer and only consider its absolute value.
"""

def complex_digit_count(num):
    even_count = odd_count = three_count = 0
    for digit in str(abs(num)):    # loop through each digit in the string representation of num
        if int(digit) % 2 == 0:    # if digit is even,
            even_count += 1         # increment even_count
        elif int(digit) % 2 != 0:   # otherwise, if digit is odd,
            odd_count += 1           # increment odd_count
        if int(digit) % 3 == 0:    # if digit is divisible by 3,
            three_count += 1         # increment three_count
    return even_count, odd_count, three_count