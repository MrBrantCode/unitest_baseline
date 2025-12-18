"""
QUESTION:
Create a function named `five_nine_twelve_corrected` that calculates the sum of all integers below the input number `n` that contain the digit 5 and are divisible by either 9 or 12. The function should take an integer `n` as input and return the calculated sum.
"""

def five_nine_twelve_corrected(n: int):
    summation = 0
    for i in range(1, n):
        if '5' in str(i) and (i % 9 == 0 or i % 12 == 0):
            summation += i
    return summation