"""
QUESTION:
Write a function named `foo` that takes a list of integers as input and returns a new list containing only the even numbers from the input list. If the input list does not contain any even numbers, the function should return an empty list.
"""

def foo(lst):
    """
    This function takes a list of integers as input and returns a new list that only contains even numbers. 
    If the input list does not contain any even numbers, the function returns an empty list.
    """
    even_lst = [] 
    for num in lst: 
        if num % 2 == 0: 
            even_lst.append(num) 
    return even_lst