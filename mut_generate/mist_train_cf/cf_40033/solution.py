"""
QUESTION:
Write a function `group_jobs_by_first_letter(jobs: List[Job]) -> Dict[str, List[str]]` that takes a list of `Job` instances as input and returns a dictionary where the keys are the first letters of the job names (in uppercase) and the values are lists of job names starting with that letter. The function should handle cases where a letter appears in the input list for the first time and cases where it has appeared before. The `Job` class has a single attribute `Name` of type string.
"""

from typing import List, Dict

def group_jobs_by_first_letter(jobs: List[dict]) -> Dict[str, List[str]]:
    grouped_jobs = {}
    for job in jobs:
        first_letter = job['Name'][0].upper()
        if first_letter in grouped_jobs:
            grouped_jobs[first_letter].append(job['Name'])
        else:
            grouped_jobs[first_letter] = [job['Name']]
    return grouped_jobs