"""
QUESTION:
Develop a function named `split_pairs` that takes a nested list of pairs as input and returns a nested list containing two lists. The first inner list should contain the first element from each pair, and the second inner list should contain the second element from each pair.
"""

def split_pairs(pairs_list):
    # Initialize two empty lists to hold the first and second elements of each pair
    first_elements = []
    second_elements = []

    # Iterate over the nested list
    for pair in pairs_list:
        # Add the first and second elements of each pair to the corresponding lists
        first_elements.append(pair[0])
        second_elements.append(pair[1])

    # Return the two lists nested in another list
    return [first_elements, second_elements]