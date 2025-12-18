"""
QUESTION:
Write a function `filter_jobs` that takes in a list of jobs, a person's name, and a condition. The function should return a list of jobs that match the person's name and satisfy the given condition. The condition is a function that takes a job as input and returns a boolean indicating whether the job meets the condition.
"""

def filter_jobs(jobs, person_name, condition):
    matching_jobs = []
    for job in jobs:
        if job.person_name == person_name and condition(job):
            matching_jobs.append(job)
    return matching_jobs