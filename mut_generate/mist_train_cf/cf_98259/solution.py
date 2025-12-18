"""
QUESTION:
Create a function `create_onboarding_process` that generates a customized onboarding process for new employees based on their department and job role. The function should take `employee_name`, `department`, and `job_role` as input parameters. It should include a set of standard onboarding steps and dynamically add department-specific and job-role-specific steps. The function should return a list of onboarding steps.

The function should also allow for easy modification and extension of department-specific and job-role-specific steps without modifying the function logic.
"""

def create_onboarding_process(employee_name, department, job_role):
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
    return onboarding_steps