"""
QUESTION:
Write a function `find_divisible_pair` that takes a list of decimal numbers and a quotient as input. Return a pair of numbers from the list that, when divided, yield the given quotient.
"""

def find_divisible_pair(numbers, quotient):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] / numbers[j] == quotient or numbers[j] / numbers[i] == quotient:
                return (numbers[i], numbers[j])
    return None