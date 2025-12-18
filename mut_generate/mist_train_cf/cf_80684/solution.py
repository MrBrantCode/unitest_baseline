"""
QUESTION:
Write a function total_match(lst1, lst2) that accepts two lists of unique strings and returns the list with the lesser total Unicode value of all characters (excluding spaces) in it, while preserving the original order of the items in each list. If the aggregate Unicode value of both lists is the same, return lst1.
"""

def entrance(lst1, lst2):
    unicode_lst1 = sum(sum(ord(ch) for ch in word.replace(' ', '')) for word in lst1)
    unicode_lst2 = sum(sum(ord(ch) for ch in word.replace(' ', '')) for word in lst2)

    if unicode_lst1 <= unicode_lst2:
        return lst1
    else:
        return lst2