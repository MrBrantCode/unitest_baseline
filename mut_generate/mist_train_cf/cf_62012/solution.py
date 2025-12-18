"""
QUESTION:
Write a function `remove_duplicates` that takes a list of dictionaries as input. The function should remove duplicate values across all dictionaries in the list while preserving the original order of appearance. The function should return the modified list of dictionaries.
"""

def remove_duplicates(lst):
    seen = set()
    for dic in lst:
        dic_copy = dic.copy()  
        for key, value in dic.items():
            if value in seen:
                del dic_copy[key] 
            else:
                seen.add(value)
        dic.clear()
        dic.update(dic_copy)
    return lst