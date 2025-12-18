"""
QUESTION:
Write a function `common_elements(groupA, groupB, groupC)` that takes three distinct mathematical collections as input and returns a dictionary with common elements as keys and their respective counts in each group as values. The function should handle collections of any length, account for potential duplicates within the collections, and return the count of each common element found in each group, disregarding the order of elements in the collections.
"""

from collections import Counter

def common_elements(groupA, groupB, groupC):
    # Create dictionaries with count of each element
    countA = Counter(groupA)
    countB = Counter(groupB)
    countC = Counter(groupC)
    
    common = {}  # Dictionary to store the common elements and their counts
    
    # Loop through each element in countA
    for element in countA:
        # If element is also in countB and countC
        if element in countB and element in countC:
            # Get the counts in each group and store in common dictionary
            common[element] = (countA[element], countB[element], countC[element])
    
    return common