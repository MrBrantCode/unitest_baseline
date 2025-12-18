"""
QUESTION:
Create a function `check_job_status(job)` that waits for a job to finish without blocking other jobs from running and utilizing system resources. The function should free up resources once the job is finished and allow the job to resume from its previous state when restarted. The job is considered finished when `job.status()` returns "finished".
"""

import concurrent.futures

def check_job_status(job):
    # Blocking until job finishes
    while True:
        if job.status() == "finished" :
            return True