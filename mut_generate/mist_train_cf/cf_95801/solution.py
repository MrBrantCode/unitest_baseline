"""
QUESTION:
Write a program that manages employee details. The program should have the following functions: 

- `create_employee(name, age)`: a function that creates an employee object with the given name and age. The employee object should be represented as a dictionary.

- `print_details(employee)`: a function that takes an employee object and returns a string containing the employee's name and age in the format "Name: {name}, age: {age}".

- `sort_employees(employees, compare_func)`: a function that takes a list of employee objects and a comparison function as parameters. The comparison function defines the ordering of the employees based on their age. The function should return a new list of employees sorted by their age in ascending order using a stable sorting algorithm with a time complexity of O(n log n). The function should not use any built-in sorting functions or methods. 

The program should not use classes. The `sort_employees` function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def create_employee(name, age):
    return {"name": name, "age": age}

def print_details(employee):
    return f"Name: {employee['name']}, age: {employee['age']}"

def sort_employees(employees, compare_func):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if compare_func(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return merge_sort(employees)