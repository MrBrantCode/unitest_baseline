"""
QUESTION:
Implement a function `generate_report(result)` that processes the `result` object and generates a report based on the check results. The `result` object has attributes `_host` and `_task`, and a method `_all_vars(host, task)`, as well as an attribute `_result` that contains a list of dictionaries in `result._result["results"]`. 

The report should include the host name and, for each check result, if the check was skipped, include "Check skipped for [host]". The function should return the generated report as a list of strings, where each string represents a line in the report.
"""

def generate_report(result):
    report = []
    host = result._host.get_name()
    report.append(f"Report for host: {host}")

    for check_result in result._result["results"]:
        skipped = check_result.get("skipped", False)
        if skipped:
            report.append(f"Check skipped for {host}")

    return report