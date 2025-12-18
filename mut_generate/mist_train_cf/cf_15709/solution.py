"""
QUESTION:
Create a function named `update_array` that takes two parameters: an array `arr` and a number `num`. The function should update all elements in `arr` by adding `num` to them, but only for elements that are divisible by 2. After updating the elements, the function should remove any duplicate elements from the array and sort the array in ascending order.
"""

def update_array(arr, num):
    updated_arr = []
    for element in arr:
        if element % 2 == 0:
            updated_arr.append(element + num)
        else:
            updated_arr.append(element)

    updated_arr = list(set(updated_arr)) 
    updated_arr.sort() 

    return updated_arr