"""
QUESTION:
Create a function `calculate_frequency` that takes a list of integers as input and returns a dictionary where the keys are the unique integers from the input list and the values are their frequencies. The input list contains 1 to 10^5 integers, each ranging from -10^9 to 10^9.
"""

def calculate_frequency(input_list):
    sequence_frequencies = {}
    for num in input_list:
        if num in sequence_frequencies:
            sequence_frequencies[num] += 1
        else:
            sequence_frequencies[num] = 1
    return sequence_frequencies