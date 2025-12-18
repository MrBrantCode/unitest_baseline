"""
QUESTION:
Create a function `advanced_file_name_validator` that takes a string denoting a file's name and returns 'VALID' if the name meets all conditions and 'INVALID' otherwise. The conditions are:
- The name consists only of alphanumeric characters with at least one uppercase letter, one lowercase letter, and one number.
- It contains between four and six sequentially ordered digits.
- A single period is mandatory and the name cannot start or end with a special character.
- The part before the period must not be empty, start with an English alphabet letter, and contain at least six characters including three distinct English alphabet letters.
- The part after the period must match these extensions: ['txt', 'exe', 'dll', 'pdf', 'jpeg', 'js', 'docx', 'xlsx', 'jpg', 'png'].
- The full name, including the dot, must be between 8 and 100 characters long.
"""

def advanced_file_name_validator(file_name):
    """
    Validate a file name based on specific conditions.

    Args:
    file_name (str): The file name to be validated.

    Returns:
    str: 'VALID' if the file name is valid, 'INVALID' otherwise.
    """

    # Check if the name contains between 8 and 100 characters
    if not 8 <= len(file_name) <= 100:
        return 'INVALID'

    # Check if the name starts or ends with a special character
    if not file_name[0].isalnum() or not file_name[-1].isalnum():
        return 'INVALID'

    # Split the name into two parts at the period
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'INVALID'

    # Check the part before the period
    before_period = parts[0]
    if not before_period[0].isalpha():
        return 'INVALID'
    if len(before_period) < 6:
        return 'INVALID'
    if len(set(c for c in before_period if c.isalpha())) < 3:
        return 'INVALID'

    # Check the part after the period
    after_period = parts[1]
    valid_extensions = ['txt', 'exe', 'dll', 'pdf', 'jpeg', 'js', 'docx', 'xlsx', 'jpg', 'png']
    if after_period not in valid_extensions:
        return 'INVALID'

    # Check for sequentially ordered digits
    for i in range(len(file_name) - 3):
        if file_name[i].isdigit() and file_name[i+1].isdigit() and file_name[i+2].isdigit() and file_name[i+3].isdigit():
            if int(file_name[i+1]) - int(file_name[i]) == 1 and int(file_name[i+2]) - int(file_name[i+1]) == 1 and int(file_name[i+3]) - int(file_name[i+2]) == 1:
                return 'VALID'

    # Check for at least one uppercase letter, one lowercase letter, and one number
    if not any(c.isupper() for c in file_name) or not any(c.islower() for c in file_name) or not any(c.isdigit() for c in file_name):
        return 'INVALID'

    return 'VALID'