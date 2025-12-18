"""
QUESTION:
Write a function named `sort_dict_objects` that takes a list of dictionary objects as input. The function should return a new list of the input dictionary objects sorted by the value of the "age" field in descending order, while excluding any objects where the "age" is less than 30. If two or more objects have the same age, they should be sorted by the value of the "name" field in ascending order. The function should have a time complexity of O(n log n), where n is the number of dictionary objects, and a space complexity of O(1), i.e., it should not use any additional space proportional to the number of dictionary objects.
"""

def sort_dict_objects(objects):
    return sorted([obj for obj in objects if obj["age"] >= 30], key=lambda x: (-x["age"], x["name"]))