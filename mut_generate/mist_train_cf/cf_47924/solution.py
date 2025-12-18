"""
QUESTION:
Create a function called `five_char_elements` that takes an array of strings as input. The function should return a new array containing only the strings from the input array that have exactly 5 characters. The function should not modify the original input array.
"""

def five_char_elements(arr):
    outputArray = []
    for element in arr:
        if len(element) == 5:
            outputArray.append(element)
    return outputArray