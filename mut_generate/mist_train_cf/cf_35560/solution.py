"""
QUESTION:
Create a function named `filter_enrollments` that filters and processes a list of enrollments based on the given parameters: `external_key` (string), `enrollment_type` (string), `state` (string), and `actions` (list of strings). The function should return a list of dictionaries, each representing an enrollment with the keys 'id' (int), 'type' (string), 'key' (string), 'recipient' (string), and 'enrolled_user' (string).
"""

from typing import List, Dict, Union

def filter_enrollments(external_key: str, enrollment_type: str, state: str, actions: List[str]) -> List[Dict[str, Union[int, str]]]:
    # Assume enrollments are retrieved and processed based on the provided parameters
    enrollments = []  # Replace with actual enrollments retrieval logic
    filtered_enrollments = []
    for x in enrollments:
        enrollment_dict = {
            'id': x.id,
            'type': x.enrollment_type,
            'key': x.external_key,
            'recipient': x.enrolled_email,
            'enrolled_user': x.enrolled_user_email if x.enrolled_user_email else '',
        }
        filtered_enrollments.append(enrollment_dict)
    return filtered_enrollments