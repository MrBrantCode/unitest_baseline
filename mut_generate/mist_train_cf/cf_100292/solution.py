"""
QUESTION:
Create a function `calculate_compensation` that calculates the compensation amount based on the Thailand Workmen Compensation Act. The function takes in the following parameters: 

- `injury_category`: an integer from 1 to 5, representing the type of injury
- `employee_wages`: a float, representing the employee's wages
- `degree_of_disability`: an integer from 1 to 100 (optional), representing the degree of disability for injury category 3
- `period_of_disability`: an integer (optional), representing the period of disability in months for injury category 4
- `dependents`: a list of strings (optional), representing the dependents for injury category 5, which can include 'spouse' and/or 'child'

The function should return the corresponding compensation amount according to the Act's provisions. If the injury category is not recognized, the function should return 0.
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