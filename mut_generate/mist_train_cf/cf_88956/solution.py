"""
QUESTION:
Write a function `count_frequencies` that takes a list of integers as input and returns the frequency of numbers divisible by 3, the frequency of numbers not divisible by 3, the sum of all numbers divisible by 3, and the product of all numbers not divisible by 3. The function should handle negative numbers and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def count_frequencies(numbers):
    freq_divisible_by_3 = 0
    freq_not_divisible_by_3 = 0
    sum_divisible_by_3 = 0
    product_not_divisible_by_3 = 1

    for number in numbers:
        if number % 3 == 0:
            freq_divisible_by_3 += 1
            sum_divisible_by_3 += number
        else:
            freq_not_divisible_by_3 += 1
            product_not_divisible_by_3 *= number

    return freq_divisible_by_3, freq_not_divisible_by_3, sum_divisible_by_3, product_not_divisible_by_3