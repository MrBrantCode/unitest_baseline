"""
QUESTION:
Create a function called `find_arithmetic_sequences` that takes a list of number sequences and a numerical entity as input. The function should append the numerical entity to each sequence and check if the resulting sequence forms an arithmetic progression. If a sequence forms an arithmetic progression after the numeric value addition, it should be added to the results list. The function should return the results list that contains all sequences that form an arithmetic progression. The numerical entity is appended at the end of each sequence.
"""

def find_arithmetic_sequences(sequences, value):
    result = []

    for sequence in sequences:
        sequence.append(value)
        
        difference = sequence[1] - sequence[0]
        
        for i in range(2, len(sequence)):
            if sequence[i] - sequence[i - 1] == difference:
                if i == len(sequence) - 1:
                    result.append(sequence[:])
            else:
                break  

    return result