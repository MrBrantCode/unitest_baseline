"""
QUESTION:
The function name should be processIterable. It should take a list or any other iterable as input, return a triplet, and handle circular references. The first component of the triplet should be a boolean value indicating whether the primary list and all its nested counterparts are empty. The second component should be an integer signifying the total count of void lists or iterables. The third component should be an integer representing the total number of elements spanning all lists or iterables. The function should also be able to handle and count the number of non-iterable objects within the lists.
"""

def processIterable(lst, checked=None):
    if checked is None:
        checked = set()
    isEmpty = True
    totalVoidIterables = 0
    totalElements = 0
    if id(lst) in checked:
        return isEmpty, totalVoidIterables, totalElements
    checked.add(id(lst))
    try:
        iter(lst)
    except TypeError as e:
        # If lst is not iterable
        return isEmpty, totalVoidIterables, totalElements + 1
    else:
        if len(lst) == 0:
            totalVoidIterables += 1
        else:
            isEmpty = False
            for element in lst:
                is_empty, void_count, element_count = processIterable(element, checked)
                isEmpty = isEmpty and is_empty
                totalVoidIterables += void_count
                totalElements += element_count
        return isEmpty, totalVoidIterables, totalElements