"""
QUESTION:
Write a function called `count_unique_employees` that takes a list of company information as input, where each company is represented as a list containing the company name followed by a list of employee names. The function should return a dictionary where the keys are the company names and the values are the number of unique employees in each company. Assume company and employee names are case-sensitive, and employees can work in multiple companies.
"""

def count_unique_employees(company_list):
    """Return a dictionary with company names as keys and the number of unique employees as values."""
    company_dict = {}
    for company in company_list:
        company_name = company[0]
        if company_name not in company_dict:
            company_dict[company_name] = set()
        for employee in company[1:]:
            company_dict[company_name].add(employee)
    return {company: len(employees) for company, employees in company_dict.items()}