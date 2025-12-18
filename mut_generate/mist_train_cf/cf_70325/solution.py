"""
QUESTION:
Create a function named `count_unique_employees` that takes in a 2D list `company_list` and a string `company_name`, where `company_list` is a list of lists containing company name, role, first name, and surname, and `company_name` is the name of the company for which to count unique employees. The function should return the total count of unique employees for the specified company, considering case sensitivity for company and employee names, and handling employees with different roles.
"""

def count_unique_employees(company_list, company_name):
    unique_employees = set()
    for record in company_list:
        if record[0] == company_name:
            unique_employees.add((record[2], record[3])) 
    return len(unique_employees)