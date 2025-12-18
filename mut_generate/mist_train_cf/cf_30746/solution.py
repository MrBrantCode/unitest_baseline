"""
QUESTION:
Implement a function `parse_readme(app, text)` that takes in the name of an application (`app`) and the content of a README file (`text`), and returns specific information based on the application. 

The function should extract and return the following information: 
- For "AppA", the installation instructions.
- For "AppB", the list of features mentioned in the README.
- For "AppC", the contact information (email addresses) of the developers.

Assume that the README file is well-structured and contains the necessary information for each application.
"""

import re

def parse_readme(app, text):
    if app == "AppA":
        start_index = text.find("INSTALLATION")
        if start_index != -1:
            return text[start_index:]
    elif app == "AppB":
        start_index = text.find("FEATURES")
        if start_index != -1:
            end_index = text.find("\n", start_index)
            return text[start_index:end_index]
    elif app == "AppC":
        start_index = text.find("CONTACT")
        if start_index != -1:
            return " ".join(re.findall(r'[\w\.-]+@[\w\.-]+', text[start_index:]))
    return ""