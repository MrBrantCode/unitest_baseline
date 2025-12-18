"""
QUESTION:
Write two functions, `count_employees` and `calculate_average_employees`, to count the number of employees for each company and calculate the average number of employees per company, respectively.

`count_employees` should take a list of lists as a parameter, where each sublist contains a company name followed by a list of employee names. The function should return a dictionary where the keys are the company names and the values are the number of employees for each company.

`calculate_average_employees` should take the same list of lists as a parameter and return the average number of employees per company.

The input list can contain an arbitrary number of companies, and each company can have an arbitrary number of employees. The company names are unique and can be assumed to be strings without spaces. The employee names are also unique within each company.
"""

def count_employees(company_list):
    """
    Counts the number of employees for each company.

    Args:
        company_list (list): A list of lists where each sublist contains a company name followed by a list of employee names.

    Returns:
        dict: A dictionary where the keys are the company names and the values are the number of employees for each company.
    """
    employee_count = {}
    for company in company_list:
        company_name = company[0]
        employee_count[company_name] = len(company) - 1
    return employee_count


def calculate_average_employees(company_list):
    """
    Calculates the average number of employees per company.

    Args:
        company_list (list): A list of lists where each sublist contains a company name followed by a list of employee names.

    Returns:
        float: The average number of employees per company.
    """
    employee_count = count_employees(company_list)
    total_employees = sum(employee_count.values())
    average_employees = total_employees / len(employee_count)
    return average_employees