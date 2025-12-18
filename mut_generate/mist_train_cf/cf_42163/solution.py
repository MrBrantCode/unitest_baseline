"""
QUESTION:
Implement a function `process_datadog_setup_code` that takes a string `code_snippet` as input, representing a series of commands and assertions related to Datadog monitoring setup. The function should return a list of tuples, where each tuple contains the action ('addition' or 'removal') and the specific configuration line affected in the INI file. The function should only consider the `assert_file_not_contains` and `assert_file_contains` lines in the code snippet to determine the changes made to the INI file.
"""

def process_datadog_setup_code(code_snippet):
    changes = []

    for line in code_snippet.split('\n'):
        if line.startswith('assert_file_not_contains'):
            config = line.split(' ')[-1][1:-1]  
            changes.append(('removal', config))
        elif line.startswith('assert_file_contains'):
            config = line.split(' ')[-1][1:-1]  
            changes.append(('addition', config))

    return changes