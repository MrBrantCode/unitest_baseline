"""
QUESTION:
Create a function called `transform` that takes a list of tuples, where each tuple contains a string and an integer. The function should return a dictionary where the strings are keys and the values are lists of strings representing the transformed integers. The transformation rules are: if the integer is even, multiply it by 3; if the integer is odd, square it; then convert the result to a string. If a key already exists in the dictionary, append the transformed integer to the existing list; otherwise, create a new list with the transformed integer.
"""

def transform(arr):
    fruit_dict = {}
    for (fruit, num) in arr:
        transformed_num = str(num * 3 if num % 2 == 0 else num ** 2)
        if fruit in fruit_dict:
            fruit_dict[fruit].append(transformed_num)
        else:
            fruit_dict[fruit] = [transformed_num]
    return fruit_dict