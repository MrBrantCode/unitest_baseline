"""
QUESTION:
Write a function `insert_into_array(arr, target)` that inserts the target integer into the array at the correct index while maintaining the ascending order of the array. If there are duplicate target integers in the array, insert the target integer immediately after the last occurrence of the target integer. The array is in ascending order and only contains integers. Return the modified array.
"""

def insert_into_array(arr, target):
    # Find the index to insert the target integer
    index = 0
    for i in range(len(arr)):
        if arr[i] <= target:
            index = i + 1

    # Insert the target integer at the correct index
    arr.insert(index, target)

    return arr