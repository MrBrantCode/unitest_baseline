"""
QUESTION:
Write a function named `intersection` that takes two lists `list1` and `list2` as input. The function should return four lists: 
- the intersection of `list1` and `list2` with duplicates preserved, 
- a list where each number from the intersection is multiplied by the number of times it's duplicated in both lists, 
- a list of numbers present in `list1` but not in `list2`, and 
- a list of numbers present in `list2` but not in `list1`. 
The function should be efficient for very large lists.
"""

def intersection(list1, list2):
    # Converting list to set for efficient operation
    set1 = set(list1)
    set2 = set(list2)

    # Finds the common elements
    common = set1 & set2

    # Generate list with duplicates 
    common_with_duplicates = [i for i in list1 if i in common] + [i for i in list2 if i in common]

    # Use list comprehension to get the desired list3
    list3 = [i*i for i in common_with_duplicates]

    # Finding elements in list1 but not in list2 and vice versa
    in_list1_not_in_list2 = [i for i in list1 if i not in common]
    in_list2_not_in_list1 = [i for i in list2 if i not in common]
    
    return sorted(common_with_duplicates), sorted(list3), sorted(in_list1_not_in_list2), sorted(in_list2_not_in_list1)