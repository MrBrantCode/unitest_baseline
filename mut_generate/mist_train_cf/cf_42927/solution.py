"""
QUESTION:
Write a function `overrideHeader` that takes two parameters: a list of strings `templates` representing custom HTML templates, and a string `newHeader` representing the new header content. The function should return a list of strings representing the modified HTML templates with the header section overridden by the new content, leaving the main and footer sections unchanged. If a template does not contain a header section, it should be left unchanged. The function should not use any external libraries or HTML parsing modules.
"""

from typing import List

def overrideHeader(templates: List[str], newHeader: str) -> List[str]:
    modified_templates = []
    for template in templates:
        start_index = template.find('<header>')
        end_index = template.find('</header>')
        if start_index != -1 and end_index != -1:
            modified_template = template[:start_index + 8] + newHeader + template[end_index:]
            modified_templates.append(modified_template)
        else:
            modified_templates.append(template)
    return modified_templates