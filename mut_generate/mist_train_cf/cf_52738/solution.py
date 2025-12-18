"""
QUESTION:
Create a function called `invert_tuple` that takes a tuple and a numerical factor as input, and returns a new tuple where the positions of all occurrences of the specified factor in the input tuple are inverted. The function should work by swapping the positions of the first and last occurrences, the second and second-to-last occurrences, and so on, of the specified factor.
"""

def invert_tuple(input_tuple, factor):
    positions = [i for i, x in enumerate(input_tuple) if x == factor]
    inverted_positions = positions[::-1]
    output_list = list(input_tuple)
    
    for pos, inverted_pos in zip(positions, inverted_positions):
        output_list[inverted_pos] = output_list[pos]
        
    return tuple(output_list)