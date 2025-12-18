"""
QUESTION:
Create a function named `add_lists` that takes two lists, `list1` and `list2`, as input. The function should ensure that both lists have the same length and that the length is greater than 2. It should return a new list where each element is the sum of the corresponding elements in `list1` and `list2`. However, if either of the corresponding elements is divisible by 3, the result should be their product instead. If both elements are divisible by 3, the result should be their sum.
"""

def add_lists(list1, list2):
    if len(list1) != len(list2) or len(list1) < 3:
        return "Both lists should have equal length and length should be greater than 2."
    
    result = []
    for i in range(len(list1)):
        if list1[i] % 3 == 0 and list2[i] % 3 == 0:
            result.append(list1[i] + list2[i])
        elif list1[i] % 3 == 0 or list2[i] % 3 == 0:
            result.append(list1[i] * list2[i])
        else:
            result.append(list1[i] + list2[i])
    
    return result