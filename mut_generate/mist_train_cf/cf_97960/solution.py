"""
QUESTION:
Write a function called `calculate_compensation` that takes as input the injury category, employee's wages, and additional details depending on the injury category, and returns the corresponding compensation amount based on the input details, according to the provisions of the Thailand Workmen Compensation Act. The injury category is an integer from 1 to 5. For injury categories 1 and 2, no additional details are required. For injury category 3, the degree of disability (an integer from 1 to 100) must be provided. For injury category 4, the period of disability (in months) must be provided. For injury category 5, the dependents (a list of strings that can include 'spouse' and/or 'child') must be provided. If the injury category is not recognized, the function should return 0.
"""

def calculate_compensation(injury_category, employee_wages, degree_of_disability=None, period_of_disability=None, dependents=None):
    if injury_category == 1:
        return 60 * employee_wages
    elif injury_category == 2:
        return 36 * employee_wages
    elif injury_category == 3:
        if degree_of_disability >= 50:
            return degree_of_disability / 100 * employee_wages
        else:
            return 0
    elif injury_category == 4:
        return 0.5 * period_of_disability * employee_wages
    elif injury_category == 5:
        if dependents is None or len(dependents) == 0:
            return 0
        else:
            total_compensation = 0
            for dependent in dependents:
                total_compensation += 0.5 * employee_wages
                if dependent == 'spouse':
                    total_compensation += 0.25 * employee_wages
                elif dependent == 'child':
                    total_compensation += 0.10 * employee_wages
            return total_compensation
    else:
        return 0