"""
QUESTION:
Given an array of whole numbers, devise a function `find_choke_point` that identifies the position of a "choke point" component. The choke point component is a constituent where the sum of all elements to the left equals the product of the elements to the right. Return the index of the choke point if it exists, otherwise return -1.
"""

def find_choke_point(lst):
    total_sum = sum(lst)
    left_sum = 0
    right_product = 1 if lst[0] != 0 else 0
    for i in range(1,len(lst)):
        left_sum += lst[i-1]
        if(lst[i]!=0):
            right_product *= lst[i]
        if left_sum == right_product:
            return i
    return -1