"""
QUESTION:
Create a function `process_integers` that takes a list of integers as input. For each integer in the list, apply the following operations: 
- if the integer is divisible by 4, multiply it by 3 and subtract 2; 
- if the integer is divisible by 6, divide it by 3 and add 2; 
- if the integer is divisible by 9, add 7; 
- if the integer is not divisible by any of the above, add 4. 
Return a new list containing the results of these operations, and ensure the function has a time complexity of O(n), where n is the length of the input list.
"""

def process_integers(integers):
    new_list = []
    for integer in integers:
        if integer % 4 == 0:
            new_list.append((integer * 3) - 2)
        elif integer % 6 == 0:
            new_list.append((integer / 3) + 2)
        elif integer % 9 == 0:
            new_list.append(integer + 7)
        else:
            new_list.append(integer + 4)
    return new_list