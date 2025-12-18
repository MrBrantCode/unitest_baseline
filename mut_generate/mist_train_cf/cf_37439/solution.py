"""
QUESTION:
Write a function `extractIncludedTemplates` that takes a string representing a Blade template as input and returns a list of included template file names. The included template file names are denoted by the `@include` directive in Blade templates, always followed by a single-quoted or double-quoted string representing the included template file. The included template file name may contain alphanumeric characters, dots, underscores, and slashes.
"""

import re

def extractIncludedTemplates(blade_template):
    included_templates = re.findall(r"@include\(['\"](.*?)['\"]\)", blade_template)
    return included_templates