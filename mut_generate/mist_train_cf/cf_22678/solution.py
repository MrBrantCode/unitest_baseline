"""
QUESTION:
Write a function `generate_fibonacci_range` that takes two parameters, `min_value` and `max_value`, representing the range of values. The function should return a list of Fibonacci numbers within the range and the sum of those numbers. The input range is valid only if `min_value` is less than `max_value`. The function should use an iterative approach to generate Fibonacci numbers with a time complexity of O(n), where n is the number of Fibonacci numbers within the given range.
"""

def generate_fibonacci_range(min_value, max_value):
    if min_value >= max_value:
        return []

    fibonacci_nums = [0, 1]
    sum_fibonacci = 0

    while fibonacci_nums[-1] < max_value:
        next_fibonacci = fibonacci_nums[-1] + fibonacci_nums[-2]
        if next_fibonacci > max_value:
            break
        fibonacci_nums.append(next_fibonacci)

    fibonacci_nums_in_range = []
    for num in fibonacci_nums:
        if num >= min_value:
            fibonacci_nums_in_range.append(num)
            sum_fibonacci += num

    return fibonacci_nums_in_range, sum_fibonacci