"""
QUESTION:
Create a function `elementwise_product_and_sum` that takes two lists `lst1` and `lst2` as input and returns a tuple containing a new list with the element-wise product of the input lists and the sum of the product list elements. If the input lists are not of the same size, return an error message.
"""

def elementwise_product_and_sum(lst1, lst2):
    if len(lst1) != len(lst2):
        return "The lists are not of the same size"
    product_list = [a*b for a, b in zip(lst1, lst2)]
    return product_list, sum(product_list)