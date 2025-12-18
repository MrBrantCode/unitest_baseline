"""
QUESTION:
Create a function `intersection` that takes in two lists (`my_list1` and `my_list2`) and a comparison function (`cmp_func`). The function should return the intersection of elements in `my_list1` and `my_list2` without sorting the lists or using built-in functions. The function must handle tuples, lists, duplicates, and nested lists and tuples, and use `cmp_func` for comparisons. The comparison function `cmp_func` should operate on individual elements of `my_list1` and `my_list2` and return 0 if two compared elements are equal.
"""

def intersection(my_list1: list, my_list2: list, cmp_func: callable):
    intersection_list = []
    
    for elem1 in my_list1:
        for elem2 in my_list2:
            if isinstance(elem1, (list, tuple)) and isinstance(elem2, (list, tuple)):
                if intersection(elem1, elem2, cmp_func):
                    intersection_list.append(elem1)
                    break
            elif not isinstance(elem1, (list, tuple)) and not isinstance(elem2, (list, tuple)):
                if cmp_func(elem1, elem2) == 0:
                    intersection_list.append(elem1)
                    break

    return intersection_list