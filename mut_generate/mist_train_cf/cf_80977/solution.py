"""
QUESTION:
Write a function `permute` that generates and prints all possible combinations of characters in a given string, with no repeated combinations allowed. The function should take a string `data`, an index `i`, the `length` of the string, and a `result` list as input.
"""

def permute(data, i, length, result):
    # base case
    if i == length: 
        print(''.join(result))
        return
    else: 
        permute(data, i + 1, length, result)   # without current index
        result.append(data[i]) 
        permute(data, i + 1, length, result)   # with current index
        result.pop()