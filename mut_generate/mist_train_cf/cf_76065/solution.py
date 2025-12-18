"""
QUESTION:
Implement a function called `highlight_keywords` that takes a line of Python code as input and returns the line with all Python keywords highlighted. The function should use the `re` module for regular expressions and highlight keywords by making them blue. The list of Python keywords is provided as `KEYWORDS`.
"""

import re

KEYWORDS = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const',
            'continue', 'default', 'double', 'do', 'else', 'enum', 'extends', 'final', 'finally', 'float',
            'for', 'if', 'implements', 'import', 'instanceof', 'int', 'interface', 'long', 'native', 'new',
            'package', 'private', 'protected', 'public', 'return', 'short', 'static', 'strictfp', 'super',
            'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'try', 'void', 'volatile', 'while']

def highlight_keywords(line):
    for keyword in KEYWORDS:
        keyword_pattern = re.compile(r'\b'+keyword+r'\b')
        line = keyword_pattern.sub('\033[34m' + keyword + '\033[0m', line)
    return line