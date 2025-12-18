"""
QUESTION:
Implement the `chunkIt` function to divide a given sequence into a specified number of chunks. The function should distribute the elements of the sequence into the chunks as evenly as possible. If the number of elements in the sequence is not evenly divisible by the number of chunks, the remaining elements should be distributed among the first few chunks. The function should take two parameters: `seq` (the sequence to be chunked) and `num` (the number of chunks). The function should return a list of chunks.
"""

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    result = []
    last = 0.0

    while last < len(seq):
        result.append(seq[int(last):int(last + avg)])
        last += avg

    return result