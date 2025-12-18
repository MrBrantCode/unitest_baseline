"""
QUESTION:
Write a function `sort_array(arr)` that takes an array of objects as input, sorts it in ascending order of the "price" property, and if two objects have the same price, sorts them in descending order of their "name" property. The function should return the sorted array. The array is guaranteed to contain objects with "name" and "price" properties.
"""

def sort_array(arr):
    arr.sort(key=lambda x: (x['price'], x['name'].lower()[::-1]))
    return arr