"""
QUESTION:
Create a function `grant_access` that takes in four parameters: `age` (integer), `password` (string), `security_answer` (string), and `fingerprint_scan` (string). The function should return a boolean value indicating whether access should be granted or not. 

The access should be granted only if the age is 21 or above, the password matches a predefined password ("random123"), the security answer matches a predefined answer ("blue") to the question "What is your favorite color?", and the fingerprint scan matches a predefined fingerprint ("FINGERPRINT123").
"""

def grant_access(age, password, security_answer, fingerprint_scan):
    generated_password = "random123"
    generated_security_answer = "blue"
    predefined_fingerprint = "FINGERPRINT123"

    if age < 21:
        return False

    return password == generated_password and security_answer == generated_security_answer and fingerprint_scan == predefined_fingerprint