"""
QUESTION:
Write a function `count_unique_email_addresses(text)` that takes a multiline text as input and returns the unique email addresses found in the text along with their count. The function should handle large input sizes efficiently and correctly identify email addresses in different formats. The output should be in the following format: 
```
Email addresses found:
- email1
- email2
...
Total unique email addresses: count
```
Use regular expressions to match email addresses in the text.
"""

import re

def count_unique_email_addresses(text):
    # Define the regular expression pattern to match email addresses
    pattern = r'[\w.-]+@[\w.-]+'

    # Compile the pattern into a regular expression object
    regex = re.compile(pattern)

    # Find all matches of the pattern within the text
    matches = regex.findall(text)

    # Remove duplicates and count unique email addresses
    unique_addresses = set(matches)
    total_unique_addresses = len(unique_addresses)

    # Return the email addresses found and the total count
    return unique_addresses, total_unique_addresses