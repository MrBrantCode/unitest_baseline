"""
QUESTION:
Write a function named `find_constrictive` that takes a list of integers as input and returns the index of the "constrictive" element, which is an element where the sum of all preceding elements equals the product of all subsequent non-zero elements. If no such element exists, return -1.
"""

def find_constrictive(lst):
    for i in range(len(lst)):
        pre = sum(lst[:i])
        post = 1
        for num in lst[i+1:]:
            post *= num
        if pre == post:
            return i
    return -1  # returns -1 if there is no constrictive element