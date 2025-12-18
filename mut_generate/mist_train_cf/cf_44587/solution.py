"""
QUESTION:
Implement a function `compare_sequences` that compares two numerical sequences `sequenceA` and `sequenceB` and returns a list of disparities between the two. The function should be able to handle sequences of large lengths (up to 10^6) and of different lengths. A disparity is defined as a pair of elements at the same index in the two sequences that are not equal, or an element in one sequence that has no corresponding element in the other sequence.
"""

def compare_sequences(sequenceA, sequenceB):
    lenA, lenB = len(sequenceA), len(sequenceB)
    disparities = []
    
    # compare upto common length
    for i in range(min(lenA, lenB)):
        if sequenceA[i] != sequenceB[i]:
            disparities.append((i, sequenceA[i], sequenceB[i]))
            
    # if sequenceA is longer
    for i in range(min(lenA, lenB), lenA):
        disparities.append((i, sequenceA[i], 'No Value'))
    
    # if sequenceB is longer
    for i in range(min(lenA, lenB), lenB):
        disparities.append((i, 'No Value', sequenceB[i]))
      
    return disparities