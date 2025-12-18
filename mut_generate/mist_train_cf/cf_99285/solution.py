"""
QUESTION:
Create a function called `remove_at_signs` that takes a string as input. The function should delete all instances of '@' that are not followed by a letter or digit, ignoring any non-ASCII characters and HTML tags. If the string contains SQL injection attempts, return an error message instead of the modified string. The resulting string should be truncated to the first 100 characters if it exceeds that length. The function should handle input strings containing a mix of ASCII and non-ASCII characters, HTML tags, and SQL injection attempts.
"""

import re

def remove_at_signs(input_string):
    if re.search(r"(?i)(drop|delete|insert|update|union|select|exec|sp_|xp_)", input_string):
        return "Error: SQL injection attempt detected."

    html_tags = re.findall(r"<[^>]*>", input_string)
    for tag in html_tags:
        input_string = input_string.replace(tag, "")

    input_string = re.sub(r"(?<![a-zA-Z0-9])@(?![a-zA-Z0-9])", "", input_string)

    if len(input_string) > 100:
        input_string = input_string[:100]

    return input_string