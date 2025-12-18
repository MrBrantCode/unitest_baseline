"""
QUESTION:
Write a function `sort_objects` that takes an array of objects as input, where each object contains "price" and "name" properties. The function should sort the array in ascending order of the "price" property. If two objects have the same "price", they should be sorted in descending order of their "name" property. The input array will always contain between 2 and 100 objects, with each "price" being a positive integer between 1 and 10,000 (inclusive), and each "name" being a string of at most 100 characters.
"""

def sort_objects(arr):
    arr.sort(key=lambda x: (x['price'], x['name'].lower()[::-1]))
    return arr