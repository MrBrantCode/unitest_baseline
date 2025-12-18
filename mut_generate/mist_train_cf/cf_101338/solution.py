"""
QUESTION:
Write a function `generate_nested_loop(depth, sequence)` that generates a nested loop structure using recursion. The function should take two parameters: `depth`, which specifies the depth of the nested loop structure, and `sequence`, which is the initial sequence to iterate over. The function should return a list of tuples, where each tuple represents one combination of loop variables. The function should use recursion to generate inner sequences for each element in the input sequence, where each inner sequence is one element shorter than the sequence of its outer loop.
"""

def generate_nested_loop(depth, sequence):
    if depth == 0:
        return [()]
    else:
        result = []
        for i in range(len(sequence)):
            inner_sequences = generate_nested_loop(depth - 1, sequence[i+1:])
            for inner_sequence in inner_sequences:
                result.append((sequence[i],) + inner_sequence)
        return result