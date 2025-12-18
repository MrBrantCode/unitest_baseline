"""
QUESTION:
Implement a function `test_conflict_detection` with the following test cases: 
1. `test_conflicting_requirements_detected`: test that when two projects have conflicting requirements, the conflict is detected.
2. `test_non_conflicting_requirements_not_detected`: test that when two projects have non-conflicting requirements, no conflict is detected.
3. `test_multiple_conflicting_requirements_detected`: test that when a project has conflicting requirements with multiple other projects, all conflicts are detected.
The function should use the `setUp` and `tearDown` methods to initialize and clean up any necessary resources for the test cases.
"""

def test_conflict_detection(project_requirements):
    conflicts = []
    for i in range(len(project_requirements)):
        for j in range(i + 1, len(project_requirements)):
            if project_requirements[i] & project_requirements[j]:
                conflicts.append((i, j))
    return conflicts