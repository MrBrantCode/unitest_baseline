"""
QUESTION:
Create a `Student` class with an initializer that takes `name`, `age`, `grade`, and `subjects`. The `subjects` should be a list of dictionaries, where each dictionary represents a subject with a 'grade' key. Implement methods `add_subject`, `remove_subject`, and `calculate_average_grade`. 

The `add_subject` method should append a subject dictionary to the `subjects` list. The `remove_subject` method should remove a subject dictionary from the `subjects` list. The `calculate_average_grade` method should return the average grade of all enrolled subjects, excluding subjects with missing or invalid grades. If no valid grades are found, it should return 0.
"""

def calculate_average_grade(subjects):
    """
    Calculate the average grade of all enrolled subjects.

    Args:
        subjects (list): A list of dictionaries, where each dictionary represents a subject with a 'grade' key.

    Returns:
        float: The average grade of all enrolled subjects, excluding subjects with missing or invalid grades.
    """
    total_grade = 0
    count = 0
    for subject in subjects:
        if subject.get("grade") is not None and isinstance(subject.get("grade"), (int, float)):
            total_grade += subject["grade"]
            count += 1
    if count > 0:
        return total_grade / count
    else:
        return 0