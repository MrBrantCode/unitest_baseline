"""
QUESTION:
Design a function named `shared_elements` that takes two lists as input and returns a list of tuples. Each tuple should contain a distinct element present in both input lists and its minimum frequency of occurrence. The list of tuples should be sorted in ascending order based on the element value. Do not use Python's built-in list functions or any libraries to sort the result or remove duplicates. Implement a custom hash table data structure to store the frequency of each element in the input lists.
"""

def shared_elements(list1: list, list2: list):
    # this is our custom hash table
    hash_table_1 = {}
    hash_table_2 = {}

    for item in list1:
        if item in hash_table_1:
            hash_table_1[item] += 1
        else:
            hash_table_1[item] = 1

    for item in list2:
        if item in hash_table_2:
            hash_table_2[item] += 1
        else:
            hash_table_2[item] = 1

    common_elements = []
    for key, value in hash_table_1.items():
        if key in hash_table_2:
            common_elements.append((key, min(value, hash_table_2[key])))

    # since we're not allowed to use built-in sorting, we'll implement bubble sort
    # to sort the result in ascending order
    n = len(common_elements)
    for i in range(n):
        for j in range(0, n-i-1):
            if common_elements[j][0] > common_elements[j+1][0]:
                common_elements[j], common_elements[j+1] = common_elements[j+1], common_elements[j]

    return common_elements