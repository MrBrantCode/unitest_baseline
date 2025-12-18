"""
QUESTION:
Implement a function called `generate_employee_table` that displays a table of employees' information. The table should have five columns: ID, name, email address, phone number, and department. The function should include the following functionalities: 

- Sorting: Allow users to sort the table by any column in ascending and descending order. Initially, the table should be sorted by ID in ascending order.
- Pagination: Display a maximum of 10 rows per page. Provide navigation buttons or links to allow users to switch between pages.
- Search: Include a search functionality that allows users to search for specific values in any column of the table. The search should be case-insensitive and return all matching rows. Display the search results in a separate table or highlight the matching cells in the original table.

The function should also consider error handling for invalid input or unexpected server responses, performance optimization for large datasets, responsive design for different devices and screen sizes, authentication and authorization to restrict access to the table based on user roles, database integration to store and retrieve employee data, and data validation to ensure data integrity.
"""

def generate_employee_table(employees, page=1, per_page=10, sort_by='ID', order='asc', search_query=''):
    """
    Generates an employee table with sorting, pagination, and search functionality.

    Args:
        employees (list): A list of dictionaries containing employee information.
        page (int, optional): The current page number. Defaults to 1.
        per_page (int, optional): The number of rows per page. Defaults to 10.
        sort_by (str, optional): The column to sort by. Defaults to 'ID'.
        order (str, optional): The sorting order. Defaults to 'asc'.
        search_query (str, optional): The search query. Defaults to ''.

    Returns:
        list: A list of employee information dictionaries matching the search query, sorted and paginated.
    """

    # Filter employees based on search query
    filtered_employees = [employee for employee in employees if search_query.lower() in str(employee).lower()]

    # Sort employees
    sorted_employees = sorted(filtered_employees, key=lambda x: x[sort_by], reverse=(order.lower() != 'asc'))

    # Paginate employees
    paginated_employees = sorted_employees[(page-1)*per_page:page*per_page]

    return paginated_employees