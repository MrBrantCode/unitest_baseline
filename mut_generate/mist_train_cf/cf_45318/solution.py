"""
QUESTION:
Write a function called `max_product_list` that takes a list of lists containing numbers as input. The function should return a tuple containing the highest product of elements in any of the sublists and a list of all sublists that achieve this highest product. The product should be rounded to 2 decimal places. The function should handle lists containing both positive and negative integers, floating point numbers, and zeros, and should return all lists in case of a tie. It should also disregard empty lists.
"""

def max_product_list(list_of_lists):
    max_product = float('-inf')
    max_lists = []

    for lst in list_of_lists:
        if len(lst) != 0:
            product = 1
            for num in lst:
                product *= num
            product = round(product, 2)
            if product == max_product:
                max_lists.append(lst)
            elif product > max_product:
                max_lists = [lst]
                max_product = product

    return max_product, max_lists