"""
QUESTION:
Write a function `countStudents(students, sandwiches)` where `students` and `sandwiches` are two integer arrays of the same length, with elements being either `0` or `1`, representing students' preferences for circular or square sandwiches and the type of sandwiches in the pile respectively. The function should return the count of students who are unable to consume their meal.

Restrictions: `1 <= students.length, sandwiches.length <= 100`, `students.length == sandwiches.length`, `sandwiches[i]` is `0` or `1`, `students[i]` is `0` or `1`.
"""

from collections import deque

def countStudents(students, sandwiches):
    students = deque(students)
    for sandwich in sandwiches:
        if sandwich not in students:
            break
        while students[0] != sandwich:
            students.rotate(-1)
        students.popleft()
    return len(students)