"""
QUESTION:
Create a function `parse_job_submission(record)` that takes a job submission record as input and returns a dictionary containing the extracted information. The function should extract the following information from the record:
- The number of GitHub stars for the project.
- The job name.
- The resource allocation specifications (number of CPUs, memory, and walltime).
- The module to be loaded for the job.

Assume that the job submission records are well-formed and contain all the required information in the specified format.
"""

import re

def parse_job_submission(record):
    result = {}
    
    # Extract GitHub stars
    stars_match = re.search(r'<gh_stars>(\d+)', record)
    if stars_match:
        result["gh_stars"] = int(stars_match.group(1))
    
    # Extract job name
    name_match = re.search(r'#PBS -N (.+)', record)
    if name_match:
        result["job_name"] = name_match.group(1)
    
    # Extract resource allocation specifications
    resource_match = re.search(r'#PBS -l select=(\d+):ncpus=(\d+):mem=([0-9a-zA-Z]+)', record)
    if resource_match:
        result["resource_allocation"] = {
            "select": int(resource_match.group(1)),
            "ncpus": int(resource_match.group(2)),
            "mem": resource_match.group(3)
        }
    
    walltime_match = re.search(r'#PBS -l walltime=(\d+:\d+:\d+)', record)
    if walltime_match:
        result["resource_allocation"]["walltime"] = walltime_match.group(1)
    
    # Extract module to be loaded
    module_match = re.search(r'module load (.+)', record)
    if module_match:
        result["module"] = module_match.group(1)
    
    return result