"""
QUESTION:
Create a function `classify_numbers` that takes a list of integers as input and returns a dictionary with six keys: "prime", "composite", "perfect_square", "positive", "negative", and "zero". The corresponding values should be lists of numbers that fit each category. A prime number is a positive integer greater than 1 with no positive divisors other than 1 and itself. A composite number is a positive integer greater than 1 with at least one positive divisor other than 1 and itself. A perfect square is a number that can be expressed as the square of an integer. The function should classify each number as positive, negative, or zero based on its sign.
"""

import math

def classify_numbers(numbers):
    classification = {
        "prime": [],
        "composite": [],
        "perfect_square": [],
        "positive": [],
        "negative": [],
        "zero": [],
    }

    for n in numbers:
        if n > 1 and all(n % dividend != 0 for dividend in range(2, int(math.sqrt(n)) + 1)):
            classification['prime'].append(n)
        elif n > 1:
            classification['composite'].append(n)

        if n >= 0 and math.isqrt(n) ** 2 == n:
            classification['perfect_square'].append(n)

        if n > 0:
            classification['positive'].append(n)
        elif n < 0:
            classification['negative'].append(n)
        else:
            classification['zero'].append(n)

    return classification