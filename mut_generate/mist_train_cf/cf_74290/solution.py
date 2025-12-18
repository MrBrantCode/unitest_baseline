"""
QUESTION:
Complete the function `total_match(lst1, lst2)` that compares two lists of strings. The function should return the list with the lower or equal total number of characters (excluding spaces) in all its strings. The comparison should be case-insensitive and duplicates should be removed from both lists. If both lists have the same total number of characters, return the first list. If more than half of the strings in either list are numeric, return an empty list.
"""

def total_match(lst1, lst2):
    lst1 = list(dict.fromkeys([i.lower() for i in lst1]))
    lst2 = list(dict.fromkeys([i.lower() for i in lst2]))
    
    lst1_no_space = [i.replace(" ", "") for i in lst1]
    lst2_no_space = [i.replace(" ", "") for i in lst2]
    
    if (sum(i.isnumeric() for i in lst1_no_space) > len(lst1_no_space)/2 or
        sum(i.isnumeric() for i in lst2_no_space) > len(lst2_no_space)/2):
        return []
    
    count1 = sum(len(i) for i in lst1_no_space)
    count2 = sum(len(i) for i in lst2_no_space)
    
    if count1 <= count2:
        return lst1
    else:
        return lst2