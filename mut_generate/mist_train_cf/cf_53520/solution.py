"""
QUESTION:
Create a function `filter_arrange_students` that takes two parameters: `students` (a dictionary where keys are student names and values are tuples of float values representing height, weight, age, and GPA) and `mins` (a tuple of minimum acceptable values for height, weight, age, and GPA). The function should return a dictionary containing students who surpass all minimum thresholds, sorted in descending order by age, and for students with the same age, in descending order by GPA, and for students with the same age and GPA, in ascending order by name.
"""

def filter_arrange_students(students, mins):
    # Filter out students who surpass the minimum thresholds in all categories
    valid_students = {
        name: info for name, info in students.items()
        if all(student_attr >= min_attr for student_attr, min_attr in zip(info, mins))
    }

    # Sort students by age (descending), GPA (descending) and name (ascending)
    sorted_students = sorted(
        valid_students.items(),
        key=lambda x: (-x[1][2], -x[1][3], x[0])
    )

    # Return sorted students as dictionary again
    return {name: info for name, info in sorted_students}