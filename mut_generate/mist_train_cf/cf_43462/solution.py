"""
QUESTION:
Write a function `max_product_list` that takes a list of lists of integers as input. The function should return a tuple containing the highest product of elements in any sublist and all sublists with this highest product. The function must handle sublists containing both positive and negative integers, as well as zero. If multiple sublists have the same highest product, all of them should be returned.
"""

def max_product_list(list_of_lists):
    max_product = float('-inf')
    max_lists = []
    for lst in list_of_lists:
        product = 1
        for num in lst:
            product *= num
        if product > max_product:
            max_product = product
            max_lists = [lst]  # Start new list of max lists
        elif product == max_product:
            max_lists.append(lst) # Append to existing list of max lists.
    return max_product, max_lists