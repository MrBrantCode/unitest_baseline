"""
QUESTION:
Implement a function `swap_odd_even` that takes as input a string `string` and a list of blocks `blocks`, where each block is a tuple of two integers representing the start and end indices of the block. The function should swap every odd character in the input string with the next even character within each block, leaving all other characters unchanged. The function should handle blocks that go out of the string bounds, overlapping blocks, and blocks with a size of zero. The indices in the blocks are 1-based, meaning the first character in the string corresponds to index 1.
"""

def swap_odd_even(string, blocks):
    arr = list(string)

    for block in blocks:
        start = block[0] - 1
        end = min(block[1], len(string))

        for i in range(start, end, 2):
            if i + 1 < len(arr):
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return ''.join(arr)