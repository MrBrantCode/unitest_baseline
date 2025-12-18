"""
QUESTION:
Write a function `total_match` that takes two lists of strings, `lst1` and `lst2`, and returns the list with a lesser or equal total number of characters, excluding spaces. The function should maintain the original order of strings and exclude any duplicates that occur in both lists. String comparisons should be case-insensitive. If both lists have the same total number of characters, the function should prefer `lst1`.
"""

def total_match(lst1, lst2):
    len1 = sum(len(word.replace(' ', '')) for word in lst1)
    len2 = sum(len(word.replace(' ', '')) for word in lst2)
    
    if len1 <= len2:
        lst = lst1
        other_lst = lst2
    else:
        lst = lst2
        other_lst = lst1

    res = []
    other_set = set(str.lower() for str in other_lst)

    for string in lst:
        if string.lower() not in other_set:
            res.append(string)
            other_set.add(string.lower())
    return res