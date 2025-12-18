"""
QUESTION:
Design a Python program with two functions: `find_highest_salary(employees)` and `sort_by_name(employees)`. The `find_highest_salary(employees)` function takes a list of dictionaries representing employees with 'name', 'age', and 'salary' as keys and returns a list of dictionaries representing the employee(s) with the highest salary. The `sort_by_name(employees)` function takes the same list of dictionaries and returns the list sorted by 'name' in ascending order. Implement the `find_highest_salary(employees)` function using the quicksort algorithm to sort the list of employees by 'salary' in descending order.
"""

def find_highest_salary(employees):
    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)
    def partition(arr, low, high):
        pivot = arr[high]["salary"]
        i = low - 1
        for j in range(low, high):
            if arr[j]["salary"] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    quicksort(employees, 0, len(employees) - 1)
    highest_salary = employees[0]["salary"]
    highest_earners = []
    for employee in employees:
        if employee["salary"] == highest_salary:
            highest_earners.append(employee)
        else:
            break
    return highest_earners