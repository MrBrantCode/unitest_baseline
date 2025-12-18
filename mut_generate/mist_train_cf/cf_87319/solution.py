"""
QUESTION:
Create a function `update_array` that takes an array of strings and a target string as arguments. Append the target string to the array if it contains the phrase "hello world" and is not already present in the array. If the target string does not contain "hello world" or is already present in the array, append "not found" instead. If the target string contains any special characters or digits, append "invalid target". Return the updated array.
"""

def update_array(arr, target):
    if not target.isalpha() or "hello world" not in target:
        return arr + ["invalid target"]
    elif target in arr:
        return arr + ["not found"]
    else:
        return arr + [target]