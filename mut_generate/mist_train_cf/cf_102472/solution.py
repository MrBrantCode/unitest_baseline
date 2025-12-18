"""
QUESTION:
Create a function `count_males(data)` that takes a list of dictionaries representing individuals with their age and gender. The function should return the number of males in the dataset whose age is between 20 and 40 (inclusive). If an individual's dictionary does not have an "age" key, consider their age as infinity. The function must have a time complexity of O(log(n)), where n is the number of individuals in the dataset.
"""

def count_males(data):
    data.sort(key=lambda x: x.get("age", float('inf')))  
    low = binary_search(data, 20)  
    high = binary_search(data, 41)  
    males = 0
    for person in data[low:high]:
        if person.get("gender") == "male":
            males += 1
    return males

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid].get("age", float('inf')) < target:
            low = mid + 1
        else:
            high = mid - 1
    return low