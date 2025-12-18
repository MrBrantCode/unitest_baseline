"""
QUESTION:
Write a function `common_elements(list1, list2)` that prints all common integer elements in two lists. The function should handle exceptions and continue without breaking if either of the lists is `None` or not a list. It should also bypass erroneous data types in the lists. The function should not print duplicate common elements.
"""

def common_elements(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        print("Both inputs should be of type list.")
        return

    if list1 is None or len(list1) == 0:
        print("List 1 is None or empty.")
        return
    elif list2 is None or len(list2) == 0:
        print("List 2 is None or empty.")
        return

    common = set()
    for i in list1:
        if isinstance(i, int):
            if i in list2 and i not in common:
                common.add(i)

    print("Common elements: ", common)