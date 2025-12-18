"""
QUESTION:
Create a function named `create_dictionary` that takes a list of integers as input. The function should return a dictionary containing only key-value pairs for even integers from the input list, where the keys are the even integers and the values are the sum of all the odd integers that come after the even integer in the list. The dictionary should only include even integers that have odd integers following them.
"""

def create_dictionary(lst):
    dictionary = {}
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i < len(lst) - 1:
            odd_sum = 0
            for j in range(i + 1, len(lst)):
                if lst[j] % 2 != 0:
                    odd_sum += lst[j]
                else:
                    break
            if odd_sum != 0:
                dictionary[lst[i]] = odd_sum
    return dictionary