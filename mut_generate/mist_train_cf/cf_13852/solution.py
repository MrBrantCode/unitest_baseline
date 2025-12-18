"""
QUESTION:
Create a function `check_algorithm_syntax` that takes an algorithm as a string input. The function should return a string indicating whether the algorithm syntax is correct or not. The algorithm is considered syntactically correct if it meets the following conditions: 
- Each step is properly indented with a multiple of 4 spaces.
- Each step ends with a colon.
- The algorithm contains at least one loop (for/while) or conditional statement (if).
"""

def check_algorithm_syntax(algorithm):
    lines = algorithm.strip().split('\n')
    
    # Loop through each line of the algorithm
    for line_num, line in enumerate(lines, start=1):
        # Remove leading/trailing whitespaces
        stripped_line = line.strip()
        
        # Check if the line is empty or a comment
        if not stripped_line or stripped_line.startswith('#'):
            continue
        
        # Check if the line is indented correctly
        indentation = line[:len(line) - len(stripped_line)]
        if len(indentation) % 4 != 0:
            return f'Syntax error at line {line_num}: Improper indentation'
        
        # Check if the line ends with a colon
        if not stripped_line.endswith(':'):
            return f'Syntax error at line {line_num}: Missing colon'
    
    # Check if there is at least one loop or conditional statement
    algorithm_body = '\n'.join(lines[1:])  # Exclude the first line (function definition)
    if 'for ' not in algorithm_body and 'while ' not in algorithm_body and 'if ' not in algorithm_body:
        return 'Syntax error: Algorithm must contain at least one loop or conditional statement'
    
    return 'Algorithm syntax is correct'