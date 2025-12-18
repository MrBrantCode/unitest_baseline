"""
QUESTION:
Well, those numbers were right and we're going to feed their ego.

Write a function, isNarcissistic, that takes in any amount of numbers and returns true if all the numbers are narcissistic. Return false for invalid arguments (numbers passed in as strings are ok).

For more information about narcissistic numbers (and believe me, they love it when you read about them) follow this link: https://en.wikipedia.org/wiki/Narcissistic_number
"""

def is_narcissistic(*values):
    def get_digits(n):
        return [int(x) for x in list(str(n))]

    def is_narc(n):
        return n == sum([x ** len(get_digits(n)) for x in get_digits(n)])

    try:
        return all((type(n) in [int, str] and is_narc(int(n)) for n in values))
    except ValueError:
        return False