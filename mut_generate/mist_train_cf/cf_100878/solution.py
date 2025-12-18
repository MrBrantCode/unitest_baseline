"""
QUESTION:
Write a function `is_authorized(user, patient_id, permission)` that checks if a user is authorized to access patient data based on their job title, department, and patient type. The function should return `True` if the user is authorized and `False` otherwise.

The function should take into account the following access control rules:

- The user must have a job title that is associated with the department and patient type of the patient.
- The user must have the required permission level (read, write, or admin) for the patient type.
- The user must belong to the department that is associated with the patient type.

The function should use the following data structures:

- `job_titles`: a dictionary that maps job titles to their associated permissions (read, write, admin).
- `departments`: a dictionary that maps departments to their associated permissions (read, write, admin).
- `patient_types`: a dictionary that maps patient types to their associated permissions (read, write, admin).

The function should also use the `patients` dictionary, which maps patient IDs to their associated data, including department and patient type.
"""

def is_authorized(user, patient_id, permission):
    # Define job titles, departments, and patient types with their associated permissions
    job_titles = {
        'doctor': {'read': True, 'write': True, 'admin': True},
        'nurse': {'read': True, 'write': True, 'admin': False},
        'pharmacist': {'read': True, 'write': False, 'admin': False},
        'technician': {'read': True, 'write': False, 'admin': False}
    }

    departments = {
        'cardiology': {'read': True, 'write': True, 'admin': True},
        'radiology': {'read': True, 'write': False, 'admin': False},
        'oncology': {'read': True, 'write': False, 'admin': False},
        'emergency': {'read': True, 'write': True, 'admin': False}
    }

    patient_types = {
        'adult': {'read': True, 'write': True, 'admin': True},
        'child': {'read': True, 'write': False, 'admin': False},
        'senior': {'read': True, 'write': False, 'admin': False},
        'pregnant': {'read': True, 'write': True, 'admin': False}
    }

    patients = {
        '1': {'department': 'cardiology', 'patient_type': 'adult'},
        '2': {'department': 'radiology', 'patient_type': 'child'},
        '3': {'department': 'oncology', 'patient_type': 'senior'},
        '4': {'department': 'emergency', 'patient_type': 'pregnant'}
    }

    # Check if the user has the required job title and department
    if user['job_title'] not in job_titles:
        return False
    if user['department'] != patients[patient_id]['department']:
        return False
    # Check if the user has access to the patient type
    if patient_types[patients[patient_id]['patient_type']][permission] and user['patient_type'] != patients[patient_id]['patient_type']:
        return False
    # Check if the user has the required permission level
    if not job_titles[user['job_title']][permission]:
        return False
    return True