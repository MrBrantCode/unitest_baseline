"""
QUESTION:
Extract the name, email address, job title, and company name from a given text content using a function named `extract_details`. The input text content is expected to be in a structured format with the name on the first line, followed by the job title and company name on the second line, and the email address on the third line. The job title and company name are separated by the word "at". Use regular expressions to extract the email address.
"""

import re

def extract_details(data):
    lines = data.strip().split("\n")

    name = lines[0].strip()
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', data)
    email = email_match.group() if email_match else None
    job_title, company_name = None, None

    if len(lines) >= 2:
        job_title, company_name = re.match(r'(.+) at (.+)', lines[1]).groups()

    return {
        "name": name,
        "email": email,
        "job_title": job_title,
        "company_name": company_name
    }