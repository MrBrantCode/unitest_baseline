"""
QUESTION:
Create a function `extract_imports` that takes a string representing Python code as input and returns a list of imported modules. The function should extract any string following the `from` or `import` keywords, up to the first encountered space or period, and only consider the first part of the module name (before any period). Assume the input code snippet follows standard Python import conventions.
"""

import re

def extract_imports(code_snippet):
    imports = []
    lines = code_snippet.split('\n')
    for line in lines:
        if line.startswith('from'):
            match = re.search(r'from\s+(\S+)', line)
            if match:
                module = match.group(1).split('.')[0]
                imports.append(module)
        elif line.startswith('import'):
            modules = re.findall(r'import\s+(\S+)', line)
            for module in modules:
                module = module.split('.')[0]
                imports.append(module)
    return imports