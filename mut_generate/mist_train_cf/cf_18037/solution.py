"""
QUESTION:
Design an `employee_search` function to find employees in a large multinational company based on different criteria such as department, salary range, and performance rating. The function should take in a dictionary `employees` containing employee information, including name, telephone number, age, address, job title, department, salary, and performance reviews, and return a list of employees that match the search criteria. 

Restrictions: The `employees` dictionary should be represented as a list of dictionaries, where each dictionary represents an employee and contains their information. The performance reviews should be represented as a list of dictionaries within each employee's dictionary. 

Example `employees` dictionary: 
[
    {
        'name': 'John Doe',
        'telephone_number': '1234567890',
        'age': 30,
        'address': '123 Main St',
        'job_title': 'Software Engineer',
        'department': 'IT',
        'salary': 60000,
        'performance_reviews': [
            {'review_date': '2022-01-01', 'rating': 'Good'},
            {'review_date': '2023-01-01', 'rating': 'Excellent'}
        ]
    },
    {
        'name': 'Jane Doe',
        'telephone_number': '9876543210',
        'age': 25,
        'address': '456 Elm St',
        'job_title': 'Marketing Manager',
        'department': 'Marketing',
        'salary': 70000,
        'performance_reviews': [
            {'review_date': '2022-01-01', 'rating': 'Excellent'},
            {'review_date': '2023-01-01', 'rating': 'Good'}
        ]
    }
]
"""

def employee_search(employees, department=None, salary_range=None, performance_rating=None):
    """
    Searches for employees based on department, salary range, and performance rating.

    Args:
    employees (list): A list of dictionaries containing employee information.
    department (str, optional): Department to search for. Defaults to None.
    salary_range (tuple, optional): Salary range to search for. Defaults to None.
    performance_rating (str, optional): Performance rating to search for. Defaults to None.

    Returns:
    list: A list of employees that match the search criteria.
    """

    # Initialize an empty list to store the search results
    search_results = []

    # Iterate over each employee in the employees list
    for employee in employees:
        # Check if the department matches the search criteria
        if department is not None and employee['department'] != department:
            continue

        # Check if the salary falls within the search range
        if salary_range is not None and (employee['salary'] < salary_range[0] or employee['salary'] > salary_range[1]):
            continue

        # Check if the performance rating matches the search criteria
        if performance_rating is not None:
            # Check if the employee has any performance reviews
            if 'performance_reviews' not in employee:
                continue
            # Check if any of the performance reviews match the search criteria
            if not any(review['rating'] == performance_rating for review in employee['performance_reviews']):
                continue

        # If all search criteria are met, add the employee to the search results
        search_results.append(employee)

    # Return the search results
    return search_results