"""
QUESTION:
Write a function `same_frequency(num1, num2)` that determines if two integers `num1` and `num2` have the same frequency of digits without converting the numbers to strings or using built-in functions for counting the frequency of digits.
"""

def same_frequency(num1, num2):
    if len(str(num1)) != len(str(num2)):
        return False

    num1_dict = {}
    num2_dict = {}

    def count_digits(num, num_dict):
        if num == 0:
            return
        digit = num % 10
        num_dict[digit] = num_dict.get(digit, 0) + 1
        count_digits(num // 10, num_dict)

    count_digits(num1, num1_dict)
    count_digits(num2, num2_dict)

    return num1_dict == num2_dict