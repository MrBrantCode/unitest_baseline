"""
QUESTION:
Write a function `constructHashtable` that constructs a hash table where the keys are the elements from two input arrays `A` and `B`, and the values hold the aggregate of occurrences from both arrays. The function should return the constructed hash table. The hash table should be able to handle duplicate elements in both arrays.
"""

def constructHashtable(A, B):
    """
    Construct a hash table from two input arrays A and B where keys are the elements 
    from both arrays and the values hold the aggregate of occurrences from both arrays.

    Args:
        A (list): The first input array.
        B (list): The second input array.

    Returns:
        dict: A hash table with keys as the elements from both arrays and values as 
        the aggregate of occurrences from both arrays.
    """

    # Initialize an empty dictionary
    hash_table = {}

    # Iterate through both arrays and update the value for each key in the dictionary
    for elem in A + B:
        if elem in hash_table:
            hash_table[elem] += 1
        else:
            hash_table[elem] = 1

    return hash_table