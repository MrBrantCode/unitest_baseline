"""
QUESTION:
Create a function named `advanced_sort_array` that takes a list of unique, positive integers as input and returns the sorted list based on the following rules:
- First, sort the integers by the count of '1's in their binary format in ascending order.
- If two numbers have the same '1's count in binary, sort them by the count of '1's in their quaternary (base 4) representation in ascending order.
- If the tie persists, sort the numbers by their values in hexadecimal representation in ascending order.
The function should not modify the original list.
"""

def advanced_sort_array(arr):
    """Sort a list of unique positive integers in ascending order based on 
    their binary and then quaternary and then hexadecimal representation"""
    # convert each integer to binary, quaternary, and hexadecimal representations and count '1's in each
    bin_counts = [[bin(i).count('1'), str(i).count('1') if len(convert_base(i, 4)) == 1 else convert_base(i, 4).count('1'), hex(i).count('1'), i] for i in arr]

    # sort list based on counts
    bin_counts.sort()

    # return sorted list of original integers
    return [i[3] for i in bin_counts]


def convert_base(num, base):
    convertString = "0123"
    if num < base:
        return convertString[num]
    else:
        return convert_base(num // base, base) + convertString[num % base]