"""
QUESTION:
Define a function named 'intersperse' that accepts a list of integers ('numbers') and an integer ('delimeter'). If the 'delimeter' is positive, the function should return a list with the 'delimeter' scattered between elements of the 'numbers' list. If the 'delimeter' is negative, the function should interpret its absolute value as a position to skip, with the sequence beginning at '1', and return the list without the 'delimeter'. The function should return an empty list when the input list is empty.
"""

def intersperse(numbers, delimeter):
    result = []
    skip = abs(delimeter) if delimeter < 0 else None
    for i, num in enumerate(numbers, start=1):
        result.append(num)
        if skip is None or i % skip != 0:
            if delimeter > 0:
                result.append(delimeter)
    if result and result[-1] == delimeter:
        result = result[:-1]
    return result