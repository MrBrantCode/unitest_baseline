"""
QUESTION:
Write a Python function named `is_authorized` to check if a user has access to patient data. The function should take in a user dictionary containing 'job_title', 'department', and 'patient_type' keys, a patient ID, and a permission level ('read', 'write', or 'admin'). The function should return True if the user is authorized to access the patient data with the given permission level and False otherwise. 

The access control system should be based on the following rules: 

- The user's job title must be in a predefined list of job titles with associated permissions.
- The user's department must be in a predefined list of departments with associated permissions.
- The user must have access to the patient type, which is determined by a predefined list of patient types with associated permissions.
- The user must have the required permission level for the job title.

Predefined data for job titles, departments, and patient types should be defined as dictionaries with the following structure:

```python
job_titles = {
    'doctor': {'read': True, 'write': True, 'admin': True},
    'nurse': {'read': True, 'write': True, 'admin': False},
    # ...
}

departments = {
    'cardiology': {'read': True, 'write': True, 'admin': True},
    'radiology': {'read': True, 'write': False, 'admin': False},
    # ...
}

patient_types = {
    'adult': {'read': True, 'write': True, 'admin': True},
    'child': {'read': True, 'write': False, 'admin': False},
    # ...
}
```
"""

# Define the list of job titles and their associated permissions
job_titles = {
    'doctor': {'read': True, 'write': True, 'admin': True},
    'nurse': {'read': True, 'write': True, 'admin': False},
    'pharmacist': {'read': True, 'write': False, 'admin': False},
    'technician': {'read': True, 'write': False, 'admin': False}
}

# Define the list of departments and their associated permissions
departments = {
    'cardiology': {'read': True, 'write': True, 'admin': True},
    'radiology': {'read': True, 'write': False, 'admin': False},
    'oncology': {'read': True, 'write': False, 'admin': False},
    'emergency': {'read': True, 'write': True, 'admin': False}
}

# Define the list of patient types and their associated permissions
patient_types = {
    'adult': {'read': True, 'write': True, 'admin': True},
    'child': {'read': True, 'write': False, 'admin': False},
    'senior': {'read': True, 'write': False, 'admin': False},
    'pregnant': {'read': True, 'write': True, 'admin': False}
}

# Define a function to check if a user is authorized to access patient data
def is_authorized(user, patient_id, permission):
    # Check if the user has the required job title
    if user['job_title'] not in job_titles:
        return False
    # Check if the user has the required department
    if user['department'] not in departments:
        return False
    # Check if the user has access to the patient type
    if user['patient_type'] not in patient_types:
        return False
    # Check if the user has the required permission level for the job title
    if not job_titles[user['job_title']][permission]:
        return False
    # Check if the user has the required permission level for the department
    if not departments[user['department']][permission]:
        return False
    # Check if the user has the required permission level for the patient type
    if not patient_types[user['patient_type']][permission]:
        return False
    return True