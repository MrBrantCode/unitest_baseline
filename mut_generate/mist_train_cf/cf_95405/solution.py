"""
QUESTION:
Create a function `grant_access` that takes in an integer `age`, a string `password`, and a string `security_answer`. The function should return a boolean indicating whether access is granted or not. The password and security answer must match predefined values ("password123" and "Smith" respectively) for access to be granted. If the age is less than 18, access should be denied.
"""

def grant_access(age, password, security_answer):
    predefined_password = "password123"
    predefined_answer = "Smith"

    if age < 18:
        return False

    return password == predefined_password and security_answer == predefined_answer