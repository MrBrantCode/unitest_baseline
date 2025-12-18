"""
QUESTION:
Implement a function named `compare_code_snippets` that compares the behavior of two code snippets. The function should take three parameters: `control_code` (the control code snippet as a string), `candidate_code` (the candidate code snippet as a string), and `inputs` (a dictionary containing the inputs to be used when executing the code snippets). The function should return a string indicating the reason for the difference in behavior between the two code snippets. The possible reasons are "old code raised, new did not", "different results", "new code raised, old did not". Assume the code snippets are syntactically correct and do not contain any syntax errors.
"""

def compare_code_snippets(control_code: str, candidate_code: str, inputs: dict) -> str:
    control_result = None
    control_exception = None
    candidate_result = None
    candidate_exception = None

    exec_globals = {}
    exec_locals = {'inputs': inputs}

    try:
        exec(control_code, exec_globals, exec_locals)
    except BaseException as e:
        control_exception = e

    control_result = exec_locals.get('control_result')

    exec_locals = {'inputs': inputs}

    try:
        exec(candidate_code, exec_globals, exec_locals)
    except BaseException as e:
        candidate_exception = e

    candidate_result = exec_locals.get('candidate_result')

    if control_exception is not None:
        return 'old code raised, new did not'
    elif control_result != candidate_result:
        return 'different results'
    elif candidate_exception is not None:
        return 'new code raised, old did not'
    else:
        return 'no difference'