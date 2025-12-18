"""
QUESTION:
Write a function `find_min_max_magnitude` that takes an array of complex numbers as input and returns two lists: the first list contains the complex number(s) with the smallest magnitude and the second list contains the complex number(s) with the largest magnitude. If multiple complex numbers have the same smallest or largest magnitude, include all of them in the corresponding list.
"""

def find_min_max_magnitude(array):
    min_magnitude_numbers = []
    max_magnitude_numbers = []
    min_magnitude = float('inf')
    max_magnitude = float('-inf')

    for number in array:
        magnitude = abs(number)

        if magnitude < min_magnitude:
            min_magnitude = magnitude
            min_magnitude_numbers = [number]
        elif magnitude == min_magnitude:
            min_magnitude_numbers.append(number)

        if magnitude > max_magnitude:
            max_magnitude = magnitude
            max_magnitude_numbers = [number]
        elif magnitude == max_magnitude:
            max_magnitude_numbers.append(number)

    return min_magnitude_numbers, max_magnitude_numbers