"""
QUESTION:
Implement a function `sort_list` that sorts an array of floating point numbers in descending order without using any built-in Python sorting functions. The function should also handle non-float elements by excluding them from the sorting process and printing an error message.
"""

def sort_list(nums):
    floats = []
    for i in nums:
        if type(i) == float:
            floats.append(i)
        else:
            print("Error: Non-float element '{}' detected and excluded.".format(i))

    length = len(floats)

    for i in range(length):
        for j in range(0, length-i-1):
            if floats[j] < floats[j+1]:
                floats[j], floats[j+1] = floats[j+1], floats[j]

    return floats