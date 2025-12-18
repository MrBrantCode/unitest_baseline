"""
QUESTION:
Create a function named `create_onboarding_process` that generates a dynamic onboarding process for new employees based on their department and job role. The function should take three parameters: `employee_name`, `department`, and `job_role`. The onboarding process should include a list of standard steps and department-specific steps, as well as additional steps based on the employee's job role. The function should print out the onboarding process and return the list of steps. The function should be flexible enough to accommodate different departments and job roles, and should be able to add or remove steps dynamically.
"""

def create_onboarding_process(employee_name, department, job_role):
    print(f"Creating onboarding process for {employee_name} in {department} department with job role {job_role}")
    onboarding_steps = ["Welcome to the company", "Introduction to team members"]
    customized_steps = {
        "IT": ["Setting up computer and software", "Security training"],
        "HR": ["Benefits enrollment", "Policy review"],
        "Sales": ["Product training", "Client outreach training"]
    }
    if department in customized_steps:
        onboarding_steps += customized_steps[department]
    if job_role == "Manager":
        onboarding_steps.append("Leadership training")
    print(f"Onboarding process for {employee_name} includes the following steps:")
    for step in onboarding_steps:
        print(step)
    return onboarding_steps