"""
QUESTION:
Create a function called `compare_list_sum` that takes two lists of integers as input and returns a string comparing their sums. The function should return "List A has a greater sum than List B" if the sum of the first list is greater, "Both lists have equal sums" if the sums are equal, and "List B has a greater sum than List A" if the sum of the second list is greater. If the inputs are not lists or contain non-integer elements, the function should return an error message.
"""

def compare_list_sum(list_A, list_B):
    
    if not isinstance(list_A, list) or not isinstance(list_B, list):
        return "Invalid input. Please provide two lists."
    
    try:
        sum_A = sum(int(i) for i in list_A)
        sum_B = sum(int(i) for i in list_B)
    except ValueError:
        return "Invalid input. One or more of the elements in the lists is not an integer."

    if sum_A > sum_B:
        return "List A has a greater sum than List B"
    elif sum_B > sum_A:
        return "List B has a greater sum than List A"
    else:
        return "Both lists have equal sums"