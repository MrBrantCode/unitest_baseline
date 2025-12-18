"""
QUESTION:
Create a function `total_match` that accepts two lists of strings, removes duplicate strings (case-insensitive), and returns the list with the lower or equal cumulative character count across its strings, excluding spaces. If both lists have the same character count, return the first list. Preserve the original order of list elements.
"""

def total_match(lst1, lst2):
    """Returns the list with the lower or equal cumulative character count across its strings, 
    excluding spaces, after removing duplicates case-insensitively."""
    
    # Remove duplicates case-insensitively
    lst1 = [s for i, s in enumerate(lst1) if s.lower() not in [x.lower() for x in lst1[:i]]]
    lst2 = [s for i, s in enumerate(lst2) if s.lower() not in [x.lower() for x in lst2[:i]]]

    # Calculate cumulative character count excluding spaces
    count1 = sum([len(s.replace(" ", "")) for s in lst1])
    count2 = sum([len(s.replace(" ", "")) for s in lst2])

    # Return the list with the lower or equal cumulative character count
    return lst1 if count1 <= count2 else lst2