"""
QUESTION:
Create a function named `find_product` that takes two parameters: a tuple of integers `seq` and an integer `target_product`. The function should generate all possible sub-sequences from `seq` (including disjointed ones) and return the first sub-sequence whose product of units equals `target_product`. If no such sub-sequence exists, return the message "No solution was found". The function should optimize the solution to avoid redundant calculations where feasible.
"""

def find_product(seq, target_product):
    """
    This function generates all possible sub-sequences from the given sequence and 
    returns the first sub-sequence whose product of units equals the target_product. 
    If no such sub-sequence exists, it returns "No solution was found".
    
    Parameters:
    seq (tuple): A tuple of integers.
    target_product (int): The target product to be achieved.
    
    Returns:
    tuple or str: The sub-sequence whose product equals the target_product, or "No solution was found" if no such sub-sequence exists.
    """

    def sub_seq(seq):
        # Base Case: Empty input sequence
        if len(seq) == 0:
            return [()]
        # Recursive Case
        else:
            # Split the input sequence into first element and the rest
            head = tuple(seq[:1])
            tail = seq[1:]
            # Recursive call
            subseqs = sub_seq(tail)
            # Combine the base sub_sequences with the new one
            new_subseqs = [ head+ss for ss in subseqs ]
            return new_subseqs + subseqs

    # Generate all sub_sequences
    all_subseq = sub_seq(seq)
    # Loop through each sub_sequence and calculate product
    for sub in all_subseq:
        product = 1
        for num in sub:
            product *= num
        # Check if product equals target product
        if product == target_product:
            return sub
    # If no sub-sequence found return error message
    return "No solution was found"