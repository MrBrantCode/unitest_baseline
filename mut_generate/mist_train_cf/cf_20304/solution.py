"""
QUESTION:
Write a function `print_powers_of_2(limit)` that prints the powers of 2 up to the given limit. The function should validate that the limit is a positive integer not exceeding 100 and ensure the sum of the printed powers of 2 does not exceed 1000. If the limit is invalid, exceeded, or the sum of powers of 2 exceeds 1000, print an error message.
"""

def print_powers_of_2(limit):
    if limit <= 0 or limit > 100:
        print("Invalid limit!")
        return
    
    power_of_2 = 1
    sum_of_powers = 0
    
    while power_of_2 <= limit and sum_of_powers + power_of_2 <= 1000:
        print(power_of_2)
        sum_of_powers += power_of_2
        power_of_2 *= 2
    
    if sum_of_powers > 1000:
        print("Sum of powers exceeds 1000!")