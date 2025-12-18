"""
QUESTION:
Write a function `max_product(lst)` that takes a list of integers as input and returns the maximum product that can be obtained from multiplying any combination of four distinct elements together. The list may contain negative numbers, zeros, and repeated elements. If the list has less than four unique elements, return a message indicating this.
"""

def max_product(lst):
    """
    Function to find the highest product that can be obtained from multiplying
    any combination of four distinct elements together.
    """
    if len(set(lst)) < 4:
        return "Less than four distinct elements present in the list"

    lst.sort() # sort the list in ascending order

    # the maximum product is either the product of the four highest numbers or
    # the product of the two smallest numbers (which may be negative) and the two highest numbers.
    return max(lst[-1] * lst[-2] * lst[-3] * lst[-4], lst[0] * lst[1] * lst[-1] * lst[-2])