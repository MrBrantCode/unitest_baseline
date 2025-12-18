"""
QUESTION:
Implement a function `validate_password(password: str, validators: List[Dict[str, str]]) -> List[str]` that takes a password and a list of validator dictionaries as input. Each validator dictionary contains the name of the validator class under the key 'NAME'. The function should apply multiple validators to the password and return a list of validation messages indicating whether the password passes each validation rule, where "Passed" means the password meets the rule and "Failed" means it doesn't.
"""

from typing import List, Dict

def validate_password(password: str, validators: List[Dict[str, str]]) -> List[str]:
    validation_messages = []
    for validator in validators:
        validator_name = validator['NAME'].split('.')[-1]  # Extracting the validator class name
        if validator_name == 'UserAttributeSimilarityValidator':
            validation_messages.append("Passed" if any(char.isdigit() for char in password) else "Failed")
        elif validator_name == 'MinimumLengthValidator':
            validation_messages.append("Passed" if len(password) >= 8 else "Failed")
        elif validator_name == 'CommonPasswordValidator':
            common_passwords = ["password", "123456", "qwerty"]
            validation_messages.append("Passed" if password not in common_passwords else "Failed")
        elif validator_name == 'NumericPasswordValidator':
            validation_messages.append("Passed" if any(char.isnumeric() for char in password) else "Failed")
    return validation_messages