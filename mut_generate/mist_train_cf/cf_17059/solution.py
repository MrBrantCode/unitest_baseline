"""
QUESTION:
Create a function named `append_target_string` that takes two arguments: an array of strings and a target string. The function should append the target string to the array if it contains the word "hello world" and is not already present in the array. If the target string does not contain "hello world" or is already present in the array, append the string "not found" instead. The function should return the updated array.
"""

def append_target_string(arr, target):
    if "hello world" in target and target not in arr:
        arr.append(target)
    else:
        arr.append("not found")
    return arr