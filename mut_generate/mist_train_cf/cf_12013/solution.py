"""
QUESTION:
Create a recursive function `multiply_list_recursive` that takes a list of integers and returns a new list where each element is multiplied by 5. The function should have a time complexity of O(n), where n is the length of the input list. The function should not use any built-in functions or libraries.
"""

def multiply_list_recursive(lst, index=0):
    if index == len(lst):
        return []
    
    multiplied_value = lst[index] * 5
    return [multiplied_value] + multiply_list_recursive(lst, index + 1)