"""
QUESTION:
Write a function `total_match(lst1, lst2)` that accepts two lists of strings. The function should return the list with a total number of characters (excluding spaces) less than or equal to the other list. If the total number of characters is the same, return the first list. Additionally, the function should remove duplicates from both lists, keeping only the first occurrence of each string, and maintain the original order of the elements.
"""

def total_match(lst1, lst2):
    # remove duplicates
    lst1 = list(dict.fromkeys(lst1))
    lst2 = list(dict.fromkeys(lst2))

    # count chars in each list
    lst1_chars = sum(len(s.replace(" ", "")) for s in lst1)
    lst2_chars = sum(len(s.replace(" ", "")) for s in lst2)

    # compare and return
    if lst1_chars <= lst2_chars:
        return lst1
    else:
        return lst2