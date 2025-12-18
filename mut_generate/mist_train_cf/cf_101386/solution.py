"""
QUESTION:
Write a function named `calculate_compensation` that calculates the compensation amount for an employee based on their job title, length of service, injury type, age, and pre-existing medical condition, with the following conditions: 

- The compensation rate is determined by the injury type, with the following rates: 
  - Death: 60 times the monthly wage
  - Permanent disability: 100 times the monthly wage
  - Total temporary disability: 70% of the daily wage for 30 days
  - Partial temporary disability: 50% of the total compensation for total temporary disability
- The compensation rate is adjusted based on the job title: 
  - Manager: 1.5 times the compensation rate
  - Supervisor: 1.25 times the compensation rate
- The compensation rate is adjusted based on the length of service: 
  - 5 years or more: 1.5 times the compensation rate
  - 2 years or more but less than 5 years: 1.25 times the compensation rate
- The compensation rate is adjusted based on the age and pre-existing medical condition: 
  - Age 60 or older, or with a pre-existing medical condition: 0.5 times the compensation rate

The function should take the injury type, job title, length of service, age, and pre-existing medical condition as inputs, and return the calculated compensation amount. Assume the monthly wage is 30,000 THB.
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