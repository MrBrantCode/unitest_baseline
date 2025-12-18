"""
QUESTION:
Write a function called sort_array that sorts an array in descending order. The function should use the built-in sort method and assign a parameter to reverse the order of the array. Ensure the parameter is correctly assigned to achieve the desired output.
"""

def sort_array(arr):
    arr.sort(reverse=True)
    return arr