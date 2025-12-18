"""
QUESTION:
Given a list of decimal numbers and a predetermined quotient, find a unique pair of numbers in the list such that when one number is divided by the other, the result equals the quotient. The function should be named `find_pair` and take two parameters: `numbers` and `quotient`. The function should return a pair of numbers if found, otherwise return `None`. Assume there is only one unique pair that satisfies the condition.
"""

def find_pair(numbers, quotient):
    for num in numbers:
        pair = num * quotient
        if pair in numbers:
            return num, pair
    return None