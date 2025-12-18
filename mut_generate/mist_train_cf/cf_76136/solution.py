"""
QUESTION:
Write a function `find_median_of_two_sorted` that takes two ordered numerical sequences `sequence1` and `sequence2` as input and returns their combined median value. The function should be able to handle sequences of any length. Assume the input sequences are already ordered, but the function does not have to take advantage of this property.
"""

def find_median_of_two_sorted(sequence1, sequence2):
    total_list = (sequence1 + sequence2)
    total_list.sort()

    n = len(total_list)
    median = 0

    if n % 2 != 0:  
        median = total_list[n//2]
    else:  
        median = (total_list[n//2 - 1] + total_list[n//2]) / 2.0

    return median