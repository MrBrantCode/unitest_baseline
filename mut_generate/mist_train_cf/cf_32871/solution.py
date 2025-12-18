"""
QUESTION:
Implement a function `process_tests` that takes a string `test_cases` containing doctest-like test cases and returns a dictionary with the results of the tests. Each test case consists of a Python expression followed by its expected output, separated by `==`. The test cases are separated by newlines. The function should evaluate the expressions, compare the results with the expected outputs, and return a dictionary where the keys are the expressions and the values are tuples containing the evaluated result and a boolean indicating whether the result matches the expected output.
"""

def process_tests(test_cases: str) -> dict:
    test_dict = {}
    lines = test_cases.split('\n')
    expr = None
    for line in lines:
        if line.startswith(">>>"):
            expr = line[4:]
        elif expr and line.strip() != "":
            expected_output = line.split("==")[1].strip()
            try:
                result = eval(expr)
                test_dict[expr] = (result, str(result) == expected_output)
            except Exception as e:
                test_dict[expr] = (None, False)
    return test_dict