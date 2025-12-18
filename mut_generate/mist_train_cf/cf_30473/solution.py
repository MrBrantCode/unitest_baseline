"""
QUESTION:
Implement a function `parseJobApplications` that takes a list of strings representing job applications in the format `<JobTitle>,<CompanyName>,<Location>,<Salary>` and returns a list of dictionaries containing the parsed information for each job application. The function should split each string into four parts and create a dictionary with keys 'JobTitle', 'CompanyName', 'Location', and 'Salary'. The input list contains strings where each string represents a job application, and the output should be a list of dictionaries where each dictionary represents a job application.
"""

from typing import List, Dict

def parseJobApplications(applications: List[str]) -> List[Dict[str, str]]:
    parsed_applications = []
    for app in applications:
        job_title, company_name, location, salary = app.split(',')
        parsed_applications.append({
            'JobTitle': job_title,
            'CompanyName': company_name,
            'Location': location,
            'Salary': salary
        })
    return parsed_applications