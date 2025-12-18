"""
QUESTION:
Implement a function `sort_dict_objects` that sorts a list of dictionary objects by the value of the "age" field in descending order, excluding any objects where the "age" is less than 30. If two or more objects have the same age, they should be sorted by the value of the "name" field in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(1) or O(n) if sorting is considered as not using extra space.
"""

def sort_dict_objects(objects):
    return [obj for obj in sorted(objects, key=lambda x: (-x["age"], x["name"])) if obj["age"] >= 30]