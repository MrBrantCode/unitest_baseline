"""
QUESTION:
Implement the `find_stride_blocks` function, which takes a list of integers as input and returns a list of tuples representing contiguous blocks of numbers with a consistent stride. The function should return a list of tuples, where each tuple contains the start index, end index, and the stride of the block. Assume that the input list will always contain at least two integers.
"""

def find_stride_blocks(numbers):
    blocks = []
    start = 0
    stride = numbers[1] - numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] != stride:
            blocks.append((start, i-1, stride))
            start = i
            stride = numbers[i] - numbers[i-1]
    
    blocks.append((start, len(numbers)-1, stride))
    return blocks