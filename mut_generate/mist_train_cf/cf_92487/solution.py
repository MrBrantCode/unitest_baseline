"""
QUESTION:
Create a function `find_armstrong_numbers` that takes two integers `lower` and `upper` as input, finds all Armstrong numbers between them (inclusive), and prints each number and the total count of Armstrong numbers found. An Armstrong number is a number such that the sum of its digits raised to the power of the number of digits is equal to the number itself. The function should handle negative lower and upper bounds as input.
"""

def find_armstrong_numbers(lower, upper):
    def is_armstrong_number(num):
        str_num = str(abs(num))
        length = len(str_num)
        sum_of_digits = sum(int(digit) ** length for digit in str_num)
        return sum_of_digits == abs(num)

    count = 0
    for num in range(lower, upper + 1):
        if is_armstrong_number(num):
            print(num)
            count += 1
    print("Total count of Armstrong numbers:", count)