"""
QUESTION:
Write a function `sort_by_age` that takes a list of employee records as input, where each record is a dictionary containing 'name', 'age', 'salary', and 'department' keys. The function should sort the list in ascending order by age and return the sorted list.
"""

def sort_by_age(employees):
    sorted_records = []
    while employees:
        record = employees.pop(0)
        inserted = False
        for i in range(len(sorted_records)):
            if record['age'] < sorted_records[i]['age']:
                sorted_records.insert(i, record)
                inserted = True
                break
        if not inserted:
            sorted_records.append(record)
    return sorted_records