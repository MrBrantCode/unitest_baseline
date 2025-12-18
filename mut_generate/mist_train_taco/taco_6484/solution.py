"""
QUESTION:
Find the difference between two collections. The difference means that either the character is present in one collection or it is present in other, but not in both. Return a sorted set with difference.

The collections can contain any character and can contain duplicates.

For instance:

A = [a,a,t,e,f,i,j]

B = [t,g,g,i,k,f]

difference = [a,e,g,j,k]
"""

def find_collection_difference(collection_a, collection_b):
    """
    Find the difference between two collections. The difference means that either the character
    is present in one collection or it is present in the other, but not in both.

    Parameters:
    collection_a (list or set): The first collection of characters.
    collection_b (list or set): The second collection of characters.

    Returns:
    set: A sorted set containing the difference between the two collections.
    """
    return sorted(set(collection_a) ^ set(collection_b))