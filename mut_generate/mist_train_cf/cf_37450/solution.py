"""
QUESTION:
Implement a function `extractAlertTypes(xmlString: str) -> List[str]` that takes an input string `xmlString` containing XML-like tags and returns a list of all "type" attribute values from `<alert>` tags in the order they appear. The "type" attribute is always enclosed in double quotes within the tag, and the input string is well-formed and contains valid XML-like tags.
"""

from typing import List
import re

def extractAlertTypes(xmlString: str) -> List[str]:
    alert_types = re.findall(r'<alert type="([^"]+)"', xmlString)
    return alert_types