"""
QUESTION:
Implement a `Student` class that encapsulates a list of grades, with methods to add, retrieve, and manipulate grades, while ensuring the list remains inaccessible from outside the class. The `add_grade` method should only accept grades between 0 and 100 (inclusive). 

Implement the following methods:
- `add_grade(grade: int) -> None`: Add a new grade to the list.
- `get_grades() -> List[int]`: Return the list of grades.
- `get_average_grade() -> float`: Return the average grade, rounded to two decimal places.
- `get_highest_grade() -> int`: Return the highest grade.
- `get_lowest_grade() -> int`: Return the lowest grade.
- `get_grade_count() -> int`: Return the total number of grades.
- `get_grade_frequency(grade: int) -> int`: Return the frequency of a specific grade.
- `get_grade_distribution() -> Dict[int, int]`: Return a dictionary of unique grades and their frequencies.
- `remove_grade(grade: int) -> None`: Remove the first occurrence of a specific grade.
"""

def student(grades, operation, grade=None):
    if operation == 'add_grade':
        if 0 <= grade <= 100:
            grades.append(grade)
    elif operation == 'get_grades':
        return grades
    elif operation == 'get_average_grade':
        if not grades:
            return 0.0
        return round(sum(grades) / len(grades), 2)
    elif operation == 'get_highest_grade':
        if not grades:
            return 0
        return max(grades)
    elif operation == 'get_lowest_grade':
        if not grades:
            return 0
        return min(grades)
    elif operation == 'get_grade_count':
        return len(grades)
    elif operation == 'get_grade_frequency':
        return grades.count(grade)
    elif operation == 'get_grade_distribution':
        distribution = {}
        for g in sorted(grades):
            distribution[g] = distribution.get(g, 0) + 1
        return distribution
    elif operation == 'remove_grade':
        if grade in grades:
            grades.remove(grade)