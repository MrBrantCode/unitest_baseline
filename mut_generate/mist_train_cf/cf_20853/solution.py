"""
QUESTION:
Create a function `convert_to_multidimensional(a)` that takes a list of integers `a` as input and returns a multidimensional list of size `len(a) x len(a)`. Each element in the multidimensional list should be a tuple containing three elements: the original element from list `a`, its index position in list `a`, and the sum of all previous elements in list `a` up to the current index position in each row.
"""

def convert_to_multidimensional(a):
    multidimensional_list = []
    for i in range(len(a)):
        row = []
        sum_previous = 0
        for j in range(len(a)):
            if j <= i:
                sum_previous += a[j]
            row.append((a[i], i, sum_previous))
        multidimensional_list.append(row)
    return multidimensional_list