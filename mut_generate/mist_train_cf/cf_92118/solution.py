"""
QUESTION:
Write a function `same_frequency` that takes two integers `num1` and `num2` as input and returns a boolean indicating whether the two numbers have the same frequency of digits. The function should not convert the numbers to strings or use any built-in functions for counting the frequency of digits.
"""

def same_frequency(num1, num2):
    digit_count1 = [0] * 10
    digit_count2 = [0] * 10

    # Count the frequency of each digit in num1
    while num1 > 0:
        digit = num1 % 10
        digit_count1[digit] += 1
        num1 //= 10

    # Count the frequency of each digit in num2
    while num2 > 0:
        digit = num2 % 10
        digit_count2[digit] += 1
        num2 //= 10

    # Check if the frequency of each digit is the same in both numbers
    for i in range(10):
        if digit_count1[i] != digit_count2[i]:
            return False

    return True