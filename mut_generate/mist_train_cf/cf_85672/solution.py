"""
QUESTION:
Create a function called `total_salary_after_deductions` that calculates the total salary after deducting the provident fund and health insurance from the basic salary. The function should take three parameters: `basic_salary`, `provident_fund_rate`, and `health_insurance_deduction`. The provident fund deduction should be calculated by multiplying the `basic_salary` by the `provident_fund_rate`. The total salary after deductions should be the `basic_salary` minus the provident fund deduction and the `health_insurance_deduction`.
"""

def total_salary_after_deductions(basic_salary, provident_fund_rate, health_insurance_deduction):
    provident_fund_deduction = basic_salary * provident_fund_rate
    total_salary = basic_salary - provident_fund_deduction - health_insurance_deduction
    return total_salary