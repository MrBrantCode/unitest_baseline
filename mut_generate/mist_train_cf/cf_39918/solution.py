"""
QUESTION:
Implement the `process_job_queue` function, which takes in a job queue and optional parameters for filtering and formatting. The job queue is a list of dictionaries, where each dictionary represents a job with various attributes. The function should filter the job queue based on the provided options and return the formatted job information.

The function should support the following options:
- `job_name`: A list of job names to be included in the view.
- `columns`: A list of columns to be shown in the view.
- `regex`: A regular expression for selecting jobs (optional).
- `recurse`: A flag to indicate whether to recurse in subfolders (default is False), although this option will not affect the job queue filtering in this function.

The function should return the filtered and formatted job information based on the specified options.
"""

import re

def process_job_queue(job_queue, job_name=None, columns=None, regex=None, recurse=False):
    filtered_jobs = job_queue

    if job_name:
        filtered_jobs = [job for job in filtered_jobs if job['job_name'] in job_name]

    if regex:
        filtered_jobs = [job for job in filtered_jobs if re.search(regex, job['job_name'])]

    if columns:
        filtered_jobs = [{col: job[col] for col in columns if col in job} for job in filtered_jobs]

    return filtered_jobs