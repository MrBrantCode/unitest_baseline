"""
QUESTION:
Create a function named `sort_and_rotate` that takes two parameters: a list of elements and an integer `n`. The function should split the list at the nth element, add the first part to the end of the second part, and then sort the resulting list in ascending order. The list can contain elements of different data types, including integers, strings, nested lists, dictionaries, and sets. The function should handle exceptions for invalid input such as when the nth element is not a valid index in the list. When sorting, the function should calculate a comparable value for each element based on its type: integers and floats are their own values, strings are their lengths, lists are the sum of their elements' values, dictionaries are the sum of their key-value pairs' values, and sets are the sum of their elements' values. If the input list is empty or the index is invalid, the function should return an error message.
"""

def sort_and_rotate(lst, n):
    if lst and n > 0 and n < len(lst):
        try:
            parts = [lst[n:], lst[:n]]
            result = sum(parts, [])
            result.sort(key=compute_sum)
            return result
        except Exception:
            return "Invalid input!"
    else:
        return "Invalid index!"

def compute_sum(elem):
    if type(elem) is int or type(elem) is float:
        return elem
    elif type(elem) is str:
        return len(elem)
    elif type(elem) is list:
        return sum(compute_sum(sub_elem) for sub_elem in elem)
    elif type(elem) is dict:
        return sum(compute_sum(k) + compute_sum(v) for k,v in elem.items())
    elif type(elem) is set:
        return sum(compute_sum(e) for e in elem)
    else:
        return 0