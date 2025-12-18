"""
QUESTION:
Develop a function `avg_salary_by_gender_and_department` that receives a table of employee details as input and returns a dictionary containing the average salary for each gender categorized by department. The input table is expected to contain the columns "Name", "Age", "Gender", "Salary", and "Department". The output dictionary should have department and gender as keys and the corresponding average salary as the value, rounded to 2 decimal places.
"""

def avg_salary_by_gender_and_department(table):
    
    avg_salaries = {}
    for row in table:
        department = row['Department']
        gender = row['Gender']
        salary = row['Salary']
        if (department, gender) in avg_salaries:
            avg_salaries[(department, gender)][0] += salary
            avg_salaries[(department, gender)][1] += 1
        else:
            avg_salaries[(department, gender)] = [salary, 1]
            
    for department, gender in avg_salaries:
        avg_salaries[(department, gender)] = round(avg_salaries[(department, gender)][0] / avg_salaries[(department, gender)][1], 2)
    
    return avg_salaries