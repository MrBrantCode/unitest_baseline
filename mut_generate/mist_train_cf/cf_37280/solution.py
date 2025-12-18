"""
QUESTION:
Implement a function `analyze_subject_data(accuracyStats, responseStats, newSubjects)` that takes in three lists of the same length: `accuracyStats`, `responseStats`, and `newSubjects`. The function should return a tuple `(averageAccuracy, mostResponsiveSubject)` where `averageAccuracy` is the average accuracy percentage rounded to two decimal places and `mostResponsiveSubject` is the subject with the highest number of responses. Assume corresponding indices in the input lists correspond to the same subject.
"""

def analyze_subject_data(accuracyStats, responseStats, newSubjects):
    """
    Analyze subject data and return the average accuracy and most responsive subject.

    Args:
        accuracyStats (list): List of accuracy percentages.
        responseStats (list): List of response statistics.
        newSubjects (list): List of subject names.

    Returns:
        tuple: A tuple containing the average accuracy and the most responsive subject.
    """
    averageAccuracy = round(sum(accuracyStats) / len(accuracyStats), 2)
    mostResponsiveSubject = newSubjects[responseStats.index(max(responseStats))]
    return (averageAccuracy, mostResponsiveSubject)