"""
QUESTION:
Create a function `extract_permissions` that takes a multi-line string `license_text` as input, extracts permissions, and returns them in a structured format. Each permission should be presented as a dictionary with keys 'Permission' and 'Rights', where 'Permission' is the verb or action, and 'Rights' is a string of associated rights or conditions. 

The function should split the input string into lines, ignore empty lines, and parse each line to extract the verb and associated rights. If a line starts with 'to' or 'and', consider the next word as the verb and the rest of the line as the rights. Return a list of extracted permissions.
"""

def extract_permissions(license_text):
    permissions = []
    lines = license_text.split('\n')
    for line in lines:
        if line.strip():  # Check if the line is not empty
            words = line.split()
            if words[0].lower() == 'to' or words[0].lower() == 'and':
                verb = words[1]
                rights = ' '.join(words[2:])
                permissions.append({'Permission': verb, 'Rights': rights})
    return permissions