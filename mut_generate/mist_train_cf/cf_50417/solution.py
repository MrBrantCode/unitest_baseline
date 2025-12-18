"""
QUESTION:
Implement a function called `cocktail_shaker_sort_separate` that sorts a list of integers using the Cocktail Shaker sort algorithm, with the following conditions: 
- All even numbers must be sorted in ascending order and placed before the odd numbers.
- All odd numbers must be sorted in ascending order.
- The function should return the sorted list.
"""

def cocktail_shaker_sort_separate(lst):
    even_lst = sorted([i for i in lst if i % 2 == 0])
    odd_lst = sorted([i for i in lst if i % 2 != 0])
    return even_lst + odd_lst