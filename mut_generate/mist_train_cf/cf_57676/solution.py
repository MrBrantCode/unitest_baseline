"""
QUESTION:
Create a function named `expunge_tup` that takes two parameters: `initial_tup` (the initial tuple of complex data structures) and `tup_to_expunge` (the tuple to be expunged). The function should return a new tuple with all instances of `tup_to_expunge` removed from `initial_tup`.
"""

def expunge_tup(initial_tup, tup_to_expunge):
    # Create an empty list to store the new tuple
    new_tup = []

    # Iterate over each element in the initial tuple
    for elem in initial_tup:
        # If the element isn't the tuple to expunge,
        # then add it to the new tuple
        if elem != tup_to_expunge:
            new_tup.append(elem)

    # Convert the list to a tuple and return result
    return tuple(new_tup)