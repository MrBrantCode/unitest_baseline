"""
QUESTION:
Write a function `find_segments(input)` that takes a string of alphabets as input and returns the count of disjoint sub-segments within the string, where each sub-segment is sorted in increasing order, along with the maximum length among these sub-segments. The input string only contains alphabets.
"""

def find_segments(input):
    input = list(map(ord, input))
    counter = 1
    max_length = 1
    length = 1
    
    for i in range(1, len(input)):
        if (input[i] > input[i-1]):
            length += 1
        else:
            max_length = max(length, max_length)
            length = 1
            counter += 1

    max_length = max(length, max_length)
    return counter, max_length