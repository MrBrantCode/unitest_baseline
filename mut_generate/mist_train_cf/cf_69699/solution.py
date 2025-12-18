"""
QUESTION:
Write a function `total_match(lst1, lst2)` that takes two lists of strings as input. The function should remove duplicates from both lists while preserving order, calculate the total characters (excluding spaces) in each list while ignoring string case, and return the list with the total characters fewer or equal to the other list. If both lists contain the same total number of characters, return the first list. However, if the total amount of numeric characters in the input lists exceeds 30% of the total characters, the function should return an empty list instead.
"""

def total_match(lst1, lst2):
    # Removing duplicates from the lists
    lst1 = sorted(set(lst1), key = lst1.index)
    lst2 = sorted(set(lst2), key = lst2.index)
    
    # Initializing character and numeric counters
    total_chars1, total_chars2, total_numeric = 0, 0, 0
    
    # Calculating characters count for lst1 and updating numeric count
    for word in lst1:
        total_chars1 += len(word.replace(" ", "").lower())
        total_numeric += sum(c.isdigit() for c in word)

    # Calculating characters count for lst2 and updating numeric count
    for word in lst2:
        total_chars2 += len(word.replace(" ", "").lower())
        total_numeric += sum(c.isdigit() for c in word)

    # Total characters in both lists
    total_chars = total_chars1 + total_chars2
    
    # Checking if numeric characters are more than 30%
    if total_numeric/total_chars > 0.3:
        return []
        
    # Return the list with fewer characters 
    if total_chars1 <= total_chars2:
        return lst1
    else:
        return lst2