"""
QUESTION:
Given an integer `n` and its reverse `r`, where `10 <= n <= 10^5` and `n` and `r` are not equal, write a function `digit_diff(n, r)` to calculate the absolute difference between the difference of the square of the sum of digits and the sum of the squares of digits for both `n` and `r`.
"""

def digit_diff(n, r):
    sum_of_squares_n = sum(int(i) ** 2 for i in str(n))
    sum_of_squares_r = sum(int(i) ** 2 for i in str(r))

    sum_of_digits_n = sum(int(i) for i in str(n))
    sum_of_digits_r = sum(int(i) for i in str(r))

    square_of_sum_n = sum_of_digits_n ** 2
    square_of_sum_r = sum_of_digits_r ** 2

    result_n = square_of_sum_n - sum_of_squares_n
    result_r = square_of_sum_r - sum_of_squares_r

    return abs(result_n - result_r)