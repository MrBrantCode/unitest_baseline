"""
QUESTION:
Implement a function `get_students` that takes a list of students and query parameters, and returns a list of students and their ages sorted in descending order of their ages. The function should filter the list of students based on the specified criteria: 
- `page` and `per_page` for pagination
- `min_age` and `max_age` for age range
- `name_filter` for name

The function should have a time complexity of O(nlogn) or better and handle pagination efficiently.
"""

def get_students(students, page, per_page, min_age, max_age, name_filter):
    """
    Returns a list of students and their ages sorted in descending order of their ages,
    filtered based on the specified criteria: page, per_page, min_age, max_age, and name_filter.

    Args:
        students (list): A list of dictionaries containing student data.
        page (int): The current page number.
        per_page (int): The number of students to display per page.
        min_age (int): The minimum age for filtering.
        max_age (int): The maximum age for filtering.
        name_filter (str): The name filter for filtering.

    Returns:
        list: A list of students and their ages sorted in descending order of their ages.
    """

    # Filter students based on age range and name
    filtered_students = [student for student in students if min_age <= student["age"] <= max_age]
    filtered_students = [student for student in filtered_students if name_filter.lower() in student["name"].lower()]

    # Sort students by age in descending order
    sorted_students = sorted(filtered_students, key=lambda student: student["age"], reverse=True)

    # Apply pagination
    start_index = (page - 1) * per_page
    end_index = start_index + per_page
    paginated_students = sorted_students[start_index:end_index]

    return paginated_students