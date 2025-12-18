"""
QUESTION:
Create a function `transform_list_complex` that takes a list of integers as input, returns a new list where each element is the input element increased by 5 if it's even, or increased by 10 if it's odd, and does not modify the original input list.
"""

def transform_list_complex(input_list):
    '''
    Transform the list by adding 5 to each element, 
    but if the element is odd, increase its value by 10
    '''
    new_list = input_list.copy()  # to prevent any side effects on the original list
    for i in range(len(new_list)):
        if new_list[i] % 2 == 0:  # If the number is even
            new_list[i] += 5
        else: # If the number is odd
            new_list[i] += 10
    return new_list