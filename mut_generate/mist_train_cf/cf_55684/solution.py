"""
QUESTION:
Create a function `find_occurrences_and_indices(numbers, number)` that takes a list of numbers and a target number as input, and returns a dictionary containing the number of occurrences of the target number and a list of indices at which the target number is present in the list.
"""

def find_occurrences_and_indices(numbers, number):
    occurrences = numbers.count(number)
    indices = [i for i, x in enumerate(numbers) if x == number]
    
    return  {'occurrences': occurrences, 'indices': indices}