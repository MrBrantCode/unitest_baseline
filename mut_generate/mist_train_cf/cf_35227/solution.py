"""
QUESTION:
Implement the function `process_sequence(seq, validbase)` to process a sequence of characters and extract valid base characters from it. The function should stop processing the sequence when a non-valid base character is encountered after at least one valid base character has been processed. The function takes two parameters: `seq` (the input sequence of characters) and `validbase` (a collection of valid base characters). It should return a string of valid base characters extracted from the input sequence.
"""

def process_sequence(seq, validbase):
    newseq = ["" for _ in seq]
    inseq = False
    lastbase = 0
    for (i, j) in enumerate(seq):
        if j in validbase:
            inseq = True
            newseq[i] = j
            lastbase = i
        elif inseq:
            break
    return "".join(newseq[:lastbase+1])