"""
QUESTION:
Write a function named `find_balance_point` that takes a list of complex numbers as input. The function must return a tuple containing the pivot point index, total number of elements, sum value, and data type of the elements in the input list. The pivot point is where the sum of the positive and negative properties to the left of the point equals the sum of the positive and negative properties to the right of the point. If the list cannot be balanced, the function should return `None`.
"""

def find_balance_point(material):
    if len(material) < 2:
        return None
    
    pos_sum = [0] * len(material)
    neg_sum = [0] * len(material)
    for i in range(1, len(material)):
        if material[i].real >= 0:
            pos_sum[i] = pos_sum[i-1] + material[i].real
            neg_sum[i] = neg_sum[i-1] + material[i].imag
        else:
            pos_sum[i] = pos_sum[i-1] + material[i].imag
            neg_sum[i] = neg_sum[i-1] + material[i].real
    
    if pos_sum[-1] != neg_sum[-1]:
        return None
    
    for i in range(1, len(material)):
        if pos_sum[i-1] == neg_sum[i-1] and pos_sum[-1] - pos_sum[i] == neg_sum[i-1]:
            return (i, len(material), pos_sum[-1], type(material[0]))
    
    return None