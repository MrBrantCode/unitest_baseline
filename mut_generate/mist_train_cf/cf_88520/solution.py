"""
QUESTION:
Write a function `same_frequency(num1, num2)` that takes two integers `num1` and `num2` and determines if they have the same frequency of digits without converting the numbers to strings or using any built-in functions for counting the frequency of digits.
"""

def same_frequency(num1, num2):
    freq1 = {}
    freq2 = {}

    def count_digits(n, freq):
        if n == 0:
            return
        digit = n % 10
        freq[digit] = freq.get(digit, 0) + 1
        count_digits(n // 10, freq)

    count_digits(num1, freq1)
    count_digits(num2, freq2)

    return freq1 == freq2