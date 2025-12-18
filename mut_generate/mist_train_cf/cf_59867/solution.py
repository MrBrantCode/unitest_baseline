"""
QUESTION:
Create a function 'find_bottleneck' that locates the index of a "bottleneck" element in a list. A bottleneck element is defined as an element where the sum of all integer elements to the left is equal to the product of the integer elements to the right. The list can contain strings, integers, and other lists, but non-integer elements and nested lists should be skipped while performing calculations. The function should return the index of the bottleneck if it exists, and -1 if no bottleneck exists in the list.
"""

def find_bottleneck(lst):
    left_sum = 0
    right_product = 1
    i = 0
    j = len(lst) - 1

    while i <= j and not isinstance(lst[i], int): 
        i += 1

    while i <= j and not isinstance(lst[j], int): 
        j -= 1

    if i > j: 
        return -1

    left_sum = lst[i]
    right_product = lst[j]

    while i < j:
        if left_sum < right_product:
            i += 1
            while i < j and not isinstance(lst[i], int): 
                i += 1
            if i < j: 
                left_sum += lst[i]
        else:
            j -= 1
            while i < j and not isinstance(lst[j], int): 
                j -= 1
            if i < j:
                right_product *= lst[j]

    return i if left_sum == right_product else -1