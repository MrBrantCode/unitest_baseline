"""
QUESTION:
Write a function `sum_list` that calculates the sum of even numbers from the input list that are divisible by 5 and contain the digit 2. The function should check each digit individually without converting the numbers to strings. The function takes a list of integers as input and returns the calculated sum.
"""

def sum_list(numbers):
    total_sum = 0
    for num in numbers:
        if num % 2 == 0 and num % 5 == 0:
            has_digit_2 = False
            temp_num = num
            while temp_num > 0:
                digit = temp_num % 10
                if digit == 2:
                    has_digit_2 = True
                    break
                temp_num = temp_num // 10
            if has_digit_2:
                total_sum += num
    return total_sum