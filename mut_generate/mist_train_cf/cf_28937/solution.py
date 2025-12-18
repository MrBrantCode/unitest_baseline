"""
QUESTION:
Implement a `runTest` method in the `TestRunner` class. This method takes a function `func` and a list of test cases `test_cases` as input where each test case is a tuple containing the input arguments for the function and the expected output. The `runTest` method should execute the function with each test case and compare the actual output with the expected output, reporting the results for each test case. The result for each test case should be a tuple containing the input arguments, the expected output, the actual output, and a string indicating whether the test case passed or failed. The method should return a list of the results for all test cases.
"""

def runTest(func, test_cases):
    results = []
    for case in test_cases:
        input_args, expected_output = case
        actual_output = func(*input_args)
        result = "Pass" if actual_output == expected_output else "Fail"
        results.append((input_args, expected_output, actual_output, result))
    return results