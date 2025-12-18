"""
QUESTION:
Implement a `TestResultsManager` class with methods to add, retrieve, and delete test results for individual students. The class should use a suitable data structure to store the test results. The methods should behave as follows:

*   `addResult(studentId, testScore)`: Add or update a test result for a student with the given `studentId` and `testScore`.
*   `getResult(studentId)`: Return the test result for a student with the given `studentId`. If the student has no test result, return -1.
*   `deleteResult(studentId)`: Remove the test result for a student with the given `studentId` if it exists.
"""

def entrance(studentId, testScore, action, results={}):
    if action == 'add':
        results[studentId] = testScore
    elif action == 'get':
        return results.get(studentId, -1)
    elif action == 'delete':
        if studentId in results:
            del results[studentId]