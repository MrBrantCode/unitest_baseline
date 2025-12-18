"""
QUESTION:
Create a function called `schedule_job` that simulates job scheduling and execution on a cluster with a total of 64 processors available for job execution. The function should take a job submission command as input, which consists of the number of processors required for the job, resource requirements specified using LSF directives, and the execution command for the job. The function should output the scheduling and execution details for the job, including whether the job was successfully scheduled or if it was rejected due to resource unavailability.

The job submission command is a string with the following format:
- The first line starts with "#BSUB -n" followed by the number of processors required for the job.
- The second line starts with "#BSUB -R" followed by the resource requirements.
- The third line is empty.
- The fourth line starts with "mpirun.lsf" followed by the execution command.

The output should be in the following format:
- "Job: <execution_command>"
- "Resource requirements: <num_processors> processors, <resource_requirements>"
- "Status: <status>" where <status> is either "Scheduled and executed successfully" or "Rejected due to resource unavailability".
"""

def schedule_job(job_submission_command):
    """
    Simulates job scheduling and execution on a cluster with a total of 64 processors available for job execution.

    Args:
        job_submission_command (str): A string representing the job submission command.

    Returns:
        str: A string containing the scheduling and execution details for the job.
    """
    # Parse the job submission command
    job_input_lines = job_submission_command.split('\n')
    num_processors = int(job_input_lines[0].split()[-1])
    resource_requirements = job_input_lines[1]
    execution_command = job_input_lines[3]

    # Simulate the cluster with 64 processors
    total_processors = 64
    available_processors = total_processors

    # Schedule the job
    status = "Scheduled and executed successfully" if num_processors <= available_processors else "Rejected due to resource unavailability"

    # Print the scheduling and execution details for the job
    output = f"Job: {execution_command}\n"
    output += f"Resource requirements: {num_processors} processors, {resource_requirements}\n"
    output += f"Status: {status}\n"

    return output