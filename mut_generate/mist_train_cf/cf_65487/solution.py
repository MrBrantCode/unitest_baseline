"""
QUESTION:
Write a function `magnify_threefold(lst)` that takes a list of numbers as input. For each number in the list, multiply it by 3. If the number is a multiple of 5 (considering only the integer part for floats and the absolute value for negatives), multiply it by 2 as well.
"""

def magnify_threefold(lst):
    return [i*3*2 if abs(int(i)) % 5 == 0 else i*3 for i in lst]