"""
QUESTION:
Write a function `find_extremes_median_mode` that takes a sequence of numbers as input, where the sequence must contain at least 15 numbers, cannot contain duplicates, and must be sorted in ascending order. The function should return the maximum, minimum, median, and mode of the numbers in the sequence. If the sequence does not meet these conditions, the function should return an error message.
"""

def find_extremes_median_mode(sequence):
    if len(sequence) < 15:
        return "Sequence must contain at least 15 numbers."
    
    if len(sequence) != len(set(sequence)):
        return "Sequence cannot contain duplicates."
    
    if sequence != sorted(sequence):
        return "Numbers in the sequence must be sorted in ascending order."
    
    maximum = max(sequence)
    minimum = min(sequence)
    
    if len(sequence) % 2 == 0:
        median = (sequence[len(sequence) // 2] + sequence[len(sequence) // 2 - 1]) / 2
    else:
        median = sequence[len(sequence) // 2]
    
    mode = None
    mode_count = 0
    current_count = 0
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            current_count = 1
        else:
            current_count += 1
        if current_count > mode_count:
            mode_count = current_count
            mode = sequence[i]
    
    return maximum, minimum, median, mode