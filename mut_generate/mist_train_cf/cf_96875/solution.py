"""
QUESTION:
Write a function `sort_objects` that sorts an array of objects in ascending order of their "price" property. If two objects have the same price, they should be sorted in descending order of their "name" property. The array contains 2-100 objects, each with a "price" property (a positive integer between 1 and 10,000) and a "name" property (a string of up to 100 characters).
"""

def sort_objects(arr):
    arr.sort(key=lambda x: (x['price'], x['name'].lower()[::-1]))
    return arr