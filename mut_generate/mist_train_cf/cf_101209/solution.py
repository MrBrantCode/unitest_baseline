"""
QUESTION:
Write a function `find_balance_point(material)` that takes a list of complex numbers `material` as input and returns a tuple containing the pivot point index, total number of elements, sum value, and data type of the elements in the input list, where the pivot point is the point in the list where the sum of the positive properties to the left equals the sum of the negative properties to the right. The function should handle edge cases such as an empty list, a list containing only one element, or a list with elements that cannot be balanced, and return `None` in these cases.
"""

def entrance(material):
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