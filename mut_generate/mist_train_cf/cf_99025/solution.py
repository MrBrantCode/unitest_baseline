"""
QUESTION:
Write a function called `generate_nested_loop` that uses recursion to generate a nested loop structure. This function should take two parameters: `depth` (the depth of the nested loop structure) and `sequence` (the initial sequence to iterate over). The function should return a list of tuples, where each tuple represents one combination of loop variables, with the length of the tuples being equal to `depth` and each tuple containing elements from `sequence`.
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