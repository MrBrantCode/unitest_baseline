"""
QUESTION:
Write a function `remove_max_from_sequence(sequence)` that takes a string of comma-separated numerical values as input. The function should return a new string where the greatest number from the input sequence is removed, while maintaining the original order and comma delineators of the remaining numbers.
"""

def remove_max_from_sequence(sequence):
    num_list = list(map(int, sequence.split(", ")))
    max_num = max(num_list)
    num_list.remove(max_num)
    return ", ".join(map(str, num_list))