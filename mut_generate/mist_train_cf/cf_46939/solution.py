"""
QUESTION:
Create a function named `segregate_array` that takes two parameters: an array of elements and an integer `n`. The function should divide the input array into `n` homogeneous sections as evenly as possible and return these sections as a list of lists. Note that due to potential integer division remainders, the last section may contain more elements than the others.
"""

def segregate_array(array, n):
    avg = len(array) / float(n)
    out = []
    last = 0.0

    while last < len(array):
        out.append(array[int(last):int(last + avg)])
        last += avg

    return out