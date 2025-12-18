"""
QUESTION:
Write a function `employee_count` that takes a list `company_list` and a `company_name` as input. The `company_list` contains sublists where the first element is the company name and the remaining elements are employee names. The function should return the number of unique employees for the specified `company_name`, considering that employees may work for multiple companies and company/employee names are case-sensitive.
"""

def employee_count(company_list, company_name):
    employee_set = set()
    for company in company_list:
        if company[0] == company_name:
            for employee in company[1:]:
                employee_set.add(employee)
    return len(employee_set)