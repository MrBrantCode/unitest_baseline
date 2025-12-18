"""
QUESTION:
Create a function named `calculate_compensation` that takes in five parameters: `injury_type`, `job_title`, `length_of_service`, `age`, and `pre_existing_condition`. The function should calculate the compensation amount for work-related injuries sustained by employees based on the type of injury, job title, length of employment, age, and pre-existing medical conditions. Assume the monthly wage is 30,000 THB. The function should return the compensation amount.
"""

def calculate_compensation(injury_type, job_title, length_of_service, age, pre_existing_condition):
    # Assume that the monthly wage is 30,000 THB
    monthly_wage = 30000
    
    # Determine the compensation rate based on injury type
    if injury_type == "Death":
        compensation_rate = 60 * monthly_wage
    elif injury_type == "Permanent disability":
        compensation_rate = 100 * monthly_wage
    elif injury_type == "Total temporary disability":
        compensation_rate = 21 * monthly_wage  # 70% of daily wage for 30 days
    else:  # Partial temporary disability
        compensation_rate = 0.5 * (21 * monthly_wage)  # 50% of total compensation for total temporary disability
    
    # Adjust compensation based on job title and length of service
    if job_title == "Manager":
        compensation_rate *= 1.5
    elif job_title == "Supervisor":
        compensation_rate *= 1.25
    
    if length_of_service >= 5:
        compensation_rate *= 1.5
    elif length_of_service >= 2:
        compensation_rate *= 1.25
    
    # Adjust compensation based on age and pre-existing condition
    if age >= 60 or pre_existing_condition:
        compensation_rate *= 0.5
    
    return compensation_rate