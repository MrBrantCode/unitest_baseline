"""
QUESTION:
Create a function named `get_allowed_actions` that takes three parameters: `role_id`, `organization_id`, and `application_id`. The function should return a list of allowed actions for the given `role_id` within the specified `organization_id` and `application_id`. The function should not modify any existing data but retrieve the allowed actions based on the input parameters. The allowed actions should be determined by the combination of `role_id`, `organization_id`, and `application_id`.
"""

def get_allowed_actions(role_id, organization_id, application_id):
    # Assuming the allowed actions are retrieved from a database or configuration
    # Here, we simulate the retrieval of allowed actions based on the input parameters
    allowed_actions = []

    # Logic to retrieve allowed actions based on role, organization, and application
    if role_id == '123' and organization_id == '456' and application_id == '789':
        allowed_actions = ['read_data', 'write_data', 'delete_data']
    elif role_id == '456' and organization_id == '789' and application_id == '123':
        allowed_actions = ['read_data', 'write_data']
    # Add more conditions as needed based on the actual business logic

    return allowed_actions