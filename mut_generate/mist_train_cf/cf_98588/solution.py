"""
QUESTION:
Create a function called `remove_at_signs` that takes a string `input_string` as an argument. The function should delete only the instances of '@' that are not followed by a digit or a letter, and return the resulting string. If the string contains any non-ASCII characters, ignore them and do not delete any '@' characters that come before or after them. If the resulting string is longer than 100 characters, truncate it to the first 100 characters. The function must also parse HTML tags before deleting the '@' characters and return an error message if the input string contains any SQL injection attempts.
"""

import re

def remove_at_signs(input_string):
    # Remove SQL injection attempts
    if re.search(r"(?i)(drop|delete|insert|update|union|select|exec|sp_|xp_)", input_string):
        return "Error: SQL injection attempt detected."
    
    # Parse HTML tags
    html_tags = re.findall(r"<[^>]*>", input_string)
    for tag in html_tags:
        input_string = input_string.replace(tag, "")
    
    # Remove '@' signs not followed by a letter or digit
    input_string = re.sub(r"(?<![a-zA-Z0-9])@(?![a-zA-Z0-9])", "", input_string)
    
    # Truncate string if it's longer than 100 characters
    if len(input_string) > 100:
        input_string = input_string[:100]
    
    return input_string