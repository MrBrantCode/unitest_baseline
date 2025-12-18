"""
QUESTION:
Write a Python function `verify_template` that checks if a given text matches a specific template. The template is defined as follows: 
- It starts with "Prompt Title: " followed by one or more characters, 
- Then two newline characters, 
- Then "Prompt Text: " followed by one or more characters, 
- Then two newline characters, 
- Then "Prompt Tags (separate by Commas): " followed by one or more characters, 
- Then two newline characters, 
- Then "Additional Information (do not edit above):" followed by two newline characters, 
- Finally, "Please generate a sentence with a advanced complexity related to the above content. Please strictly only generate sentence without any other additional text." 
The function should return `True` if the text matches the template, and `False` otherwise.
"""

import re

def verify_template(text):
    pattern = r"^Prompt Title: .*\n\nPrompt Text: .*\n\nPrompt Tags \(separate by Commas\): .*\n\nAdditional Information \(do not edit above\):\n\nPlease generate a sentence with a advanced complexity related to the above content\. Please strictly only generate sentence without any other additional text\.$"
    if re.match(pattern, text, re.MULTILINE | re.DOTALL):
        return True
    else:
        return False