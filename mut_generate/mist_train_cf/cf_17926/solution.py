"""
QUESTION:
Implement the `insertion_sort` function to sort an array of objects based on the following criteria: 
- First, sort by 'name' in ascending order.
- If two objects have the same 'name', sort by 'age' in descending order.
- If two objects have the same 'name' and 'age', sort by 'score' in descending order.
Use the insertion sort algorithm and do not use any built-in sorting functions.
"""

def insertion_sort(arr):
    def compare_objects(obj1, obj2):
        if obj1['name'] != obj2['name']:
            return -1 if obj1['name'] < obj2['name'] else 1
        elif obj1['age'] != obj2['age']:
            return -1 if obj1['age'] > obj2['age'] else 1
        else:
            return -1 if obj1['score'] > obj2['score'] else 1

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare_objects(arr[j], key) > 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr