"""
QUESTION:
Create a function `uncommon_elements` that takes a sequence of integers as input. The function should return a list of integers that appear only once in the sequence.
"""

def uncommon_elements(sequence):
    frequency = {}
    for integer in sequence:
        if integer in frequency:
            frequency[integer] += 1
        else:
            frequency[integer] = 1

    uncommon = []
    for integer, freq in frequency.items():
        if freq == 1:
            uncommon.append(integer)

    return uncommon