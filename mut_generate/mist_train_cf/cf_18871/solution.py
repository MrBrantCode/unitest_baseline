"""
QUESTION:
Create a function called `grant_access` that takes three parameters: `age`, `password`, and `security_answer`. The function should return a boolean value indicating whether access to restricted content is granted or denied. The function must meet the following conditions: 
- The `password` parameter must match the predefined password "password123".
- The `security_answer` parameter must match the predefined answer "Smith".
- If the `age` is less than 18, the function must return False regardless of the `password` and `security_answer` values.
- Both `password` and `security_answer` parameters are strings.
"""

def grant_access(age, password, security_answer):
    predefined_password = "password123"
    predefined_answer = "Smith"

    if age < 18:
        return False

    if password == predefined_password and security_answer == predefined_answer:
        return True

    return False