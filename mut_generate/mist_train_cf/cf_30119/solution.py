"""
QUESTION:
Implement the `aggregate_test_results` function, which takes a list of test results as input and returns the aggregated results. Each test result is a dictionary with keys "test_name" (string), "status" (string, either "passed" or "failed"), and "reruns" (integer, representing the number of reruns for the test). The function should aggregate the results based on the following criteria:
- If a test has failed and has reruns, the final status should be "passed" if any of the reruns pass, and "failed" if all reruns fail.
- If a test has failed but has no reruns, the final status should remain "failed".
- If a test has passed, the final status should remain "passed".
"""

from typing import List, Dict, Union

def aggregate_test_results(test_results: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    aggregated_results = []
    for test in test_results:
        if test["status"] == "failed" and test["reruns"] > 0:
            rerun_statuses = ["failed" for _ in range(test["reruns"])]
            if "passed" in rerun_statuses:
                test["status"] = "passed"
        aggregated_results.append(test)
    return aggregated_results