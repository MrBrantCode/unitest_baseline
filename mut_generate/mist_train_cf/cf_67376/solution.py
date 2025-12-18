"""
QUESTION:
Implement a function `check_order(lst)` that checks if a given list `lst` is ordered in increasing order, considering the elements can be of varying types (integers, floats, and strings). The function should return a message indicating if the list is sorted or not. If the list is not sorted, include the indices of the elements that disrupt the increasing order. 

In comparing elements, use the following rules: 
- If both elements are strings, compare them lexicographically.
- If only one element is a string, try to convert it to a float for comparison. If conversion fails, treat the string as larger than any number.
- If neither element is a string, compare them normally.
"""

def check_order(lst):
    def compare(a, b):
        if isinstance(a, str) and isinstance(b, str):
            return a > b
        elif isinstance(a, str):
            try:
                return float(a) > b
            except ValueError:
                return True
        elif isinstance(b, str):
            try:
                return a > float(b)
            except ValueError:
                return True
        else:
            return a > b

    flag = False
    indices = []
    for i in range(len(lst) - 1):
        if compare(lst[i], lst[i + 1]):
            flag = True
            indices.append(i + 1)
    if flag:
        return f"The list is not sorted. The elements at indices {indices} disrupt the order."
    else:
        return "The list is sorted."