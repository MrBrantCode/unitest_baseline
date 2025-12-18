"""
QUESTION:
Create a function `segregate_sort` that takes a list of integers as input and segregates it into two lists: one containing numbers less than or equal to 5 and another containing numbers greater than 5. The function should return both lists, each sorted in ascending order.
"""

def segregate_sort(lst):
    smaller = [i for i in lst if i <= 5]
    larger = [i for i in lst if i > 5]
    return sorted(smaller), sorted(larger)