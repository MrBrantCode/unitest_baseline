"""
QUESTION:
Create a function named `create_groups` that takes a list of `Job` objects and an integer `K` as input. The function should group the `Job` objects by their `job_type` property, with a maximum group size of `K`, and return a list of tuples containing the `Job` object's unique identifier, `job_type`, and assigned group identifier. The groups should be as equally balanced as possible.
"""

def create_groups(jobs, K):
    job_dict = {}

    # create a dictionary to store the jobs with their job_type as the key
    for job in jobs:
        if job.job_type not in job_dict:
            job_dict[job.job_type] = []
        job_dict[job.job_type].append(job)

    # sort the dictionary based on the number of job instances in each job_type
    sorted_dict = sorted(job_dict.items(), key=lambda x: len(x[1]))

    group_id = 1
    result = []

    # loop through the sorted dictionary
    for job_type, job_list in sorted_dict:

        # divide the list of job instances into groups of size K, if possible
        for i in range(0, len(job_list), K):
            group = job_list[i:i+K]
            # assign each group a unique group identifier
            for job in group:
                result.append((job.id, job_type, group_id))
            group_id += 1
    
    return result