"""
QUESTION:
Implement a `VimLParserLint` class with a method `parse_loclist` that takes a list of error messages and a line number as input. The error messages are in the format `<file_path>:<line_number>:<column_number>: vimlparser: <error_code>: <error_description>`. The method should extract the file path, line number, error code, and error description from the input message and return a JSON string representing this information for error messages where the line number matches the input line number.
"""

import json

def parse_loclist(messages, line_number):
    parsed_errors = []
    for msg in messages:
        parts = msg.split(':')
        file_path = parts[0]
        error_line = int(parts[1])
        error_column = int(parts[2])
        error_code = parts[4].strip()
        error_description = ':'.join(parts[5:]).strip()

        if error_line == line_number:
            parsed_errors.append({
                "file_path": file_path,
                "error_line": error_line,
                "error_column": error_column,
                "error_code": error_code,
                "error_description": error_description
            })

    return json.dumps(parsed_errors)