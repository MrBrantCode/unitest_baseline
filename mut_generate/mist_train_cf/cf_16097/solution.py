"""
QUESTION:
Write a function called `sum_of_elements` that takes a 2D list of integers as input. The function should calculate the sum of the second and third elements of each sublist (index 1 and 2) without using the '+' operator or any built-in Python function for addition. Instead, use only bitwise operators and loops. The function should return a list of the sums.
"""

def sum_of_elements(my_list):
    sums = []
    for sublist in my_list:
        sum = 0
        for i in range(len(sublist)):
            if i == 1:
                sum |= sublist[i]
            if i == 2:
                sum ^= sublist[i]
        sums.append(sum)
    return sums