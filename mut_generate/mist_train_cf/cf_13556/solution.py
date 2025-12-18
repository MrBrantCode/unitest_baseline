"""
QUESTION:
Create a function `sort_by_age` that takes a list of dictionaries as input, where each dictionary contains a person's information with keys "name", "age", and "city". The function should return a new list of dictionaries sorted by the person's age in descending order. You are not allowed to use built-in sort functions. The function should implement a sorting algorithm, such as bubble sort, to achieve this. The input list is expected to be non-empty and contain only dictionaries with the specified keys.
"""

def sort_by_age(persons):
    # bubble sort algorithm
    n = len(persons)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if persons[j]["age"] < persons[j + 1]["age"]:
                persons[j], persons[j + 1] = persons[j + 1], persons[j]
    return persons