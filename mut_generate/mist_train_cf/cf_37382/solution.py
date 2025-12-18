"""
QUESTION:
Write a function `extractLicense` that takes a string representing the source code file as input and returns the extracted license text. The input string will contain the entire content of the source code file. The license text is enclosed within comment delimiters, which are specified by the following patterns: 
- For single-line comments, the license text is enclosed within `//` at the beginning of the line.
- For multi-line comments, the license text is enclosed within `/*` and `*/`. 
If the license text is not found, the function should return an empty string.
"""

def extractLicense(source_code):
    lines = source_code.split('\n')
    license_text = ''
    in_multi_line_comment = False

    for line in lines:
        line = line.strip()
        if line.startswith('/*'):
            in_multi_line_comment = True
            line = line.lstrip('/*').strip()
        if in_multi_line_comment:
            if line.endswith('*/'):
                in_multi_line_comment = False
                line = line.rstrip('*/').strip()
            license_text += line + '\n'
        elif line.startswith('//'):
            license_text = line.lstrip('//').strip()
            break

    return license_text.strip()