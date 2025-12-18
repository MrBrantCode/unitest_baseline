"""
QUESTION:
Write a Python function `compare_lexicographically` that compares two sets of string entities, EntitySet1 and EntitySet2, to determine which set comes first in lexicographic ordering based on the English alphabetic system. The function should take two lists of strings as input, arrange them in lexicographic order if they are not already, and then return a string stating which set comes first.
"""

def compare_lexicographically(EntitySet1, EntitySet2):
    EntitySet1 = sorted(EntitySet1)
    EntitySet2 = sorted(EntitySet2)

    if EntitySet1 < EntitySet2:
        return "EntitySet1 comes first in lexicographic order."
    elif EntitySet1 > EntitySet2:
        return "EntitySet2 comes first in lexicographic order."
    else:
        return "EntitySet1 and EntitySet2 are in the same lexicographic order."