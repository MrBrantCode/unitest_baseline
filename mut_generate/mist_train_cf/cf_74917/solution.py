"""
QUESTION:
Write a function named `expanded_form` that takes an integer as input, and returns its expanded form as a string. The expanded form represents the number as the sum of the products of each non-zero digit and its place value. For example, the number 270240 in expanded form is '200000 + 70000 + 200 + 40'.
"""

def expanded_form(num):
    num_str = str(num)
    num_len = len(num_str)

    result = []
    for i, n in enumerate(num_str):
        if n != '0':
            result.append(n + '0' * (num_len - i - 1))

    return ' + '.join(result)