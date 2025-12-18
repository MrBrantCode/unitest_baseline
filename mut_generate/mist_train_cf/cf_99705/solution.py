"""
QUESTION:
Design a Python program with two functions: `find_highest_salary` and `sort_by_name`. The `find_highest_salary` function should take a list of dictionaries containing employee information (name, age, and salary) as input and return a list of dictionaries of the employee(s) with the highest salary. The list of employees should be sorted by salary in descending order using the quicksort algorithm. The `sort_by_name` function should sort the list of employees by name in ascending order.
"""

def partition(arr, low, high):
    pivot = arr[high]["salary"]
    i = low - 1
    for j in range(low, high):
        if arr[j]["salary"] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def find_highest_salary(employees):
    quicksort(employees, 0, len(employees) - 1)
    highest_salary = employees[0]["salary"]
    highest_earners = []
    for employee in employees:
        if employee["salary"] == highest_salary:
            highest_earners.append(employee)
        else:
            break
    return highest_earners