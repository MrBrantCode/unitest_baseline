"""
QUESTION:
Generate a function `generate_qsub_commands` that takes in four parameters: `script_name` (string), `start_range` (integer), `end_range` (integer), and `num_jobs` (integer). The function should divide the range from `start_range` to `end_range` equally among `num_jobs` and generate a list of `qsub` commands, each corresponding to a job that processes a specific range of data. The `qsub` command should follow the format: `qsub -V -cwd -q flavor.q -S /bin/bash -N <job_name> runOne.sh <script_name> <start_range> <end_range>`, where `<job_name>` is in the format `j<start_range>_<end_range>`.
"""

def generate_qsub_commands(script_name, start_range, end_range, num_jobs):
    commands = []
    range_size = (end_range - start_range) // num_jobs
    for i in range(num_jobs):
        job_start = start_range + i * range_size
        job_end = job_start + range_size
        if i == num_jobs - 1:  
            job_end = end_range
        job_name = f"j{job_start}_{job_end}"
        qsub_command = f"qsub -V -cwd -q flavor.q -S /bin/bash -N {job_name} runOne.sh {script_name} {job_start} {job_end}"
        commands.append(qsub_command)
    return commands