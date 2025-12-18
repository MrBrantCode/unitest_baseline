"""
QUESTION:
Implement a `validate_transaction` function that validates a transaction based on the provided action and artifact ID. The function should take two parameters: `action` (string) and `artifact_id` (string). It should raise an `InvalidAction` exception if the action is not one of "create", "update", or "delete", and raise an `InvalidTransaction` exception if the artifact ID is empty or None. If both the action and artifact ID are valid, the function should return True.
"""

class InvalidAction(Exception):
    pass

class InvalidTransaction(Exception):
    pass

def validate_transaction(action, artifact_id):
    valid_actions = ["create", "update", "delete"]
    
    if action not in valid_actions:
        raise InvalidAction(f"Invalid action '{action}' is not a valid action.")
    
    if not artifact_id:
        raise InvalidTransaction("Artifact ID is required")
    
    return True