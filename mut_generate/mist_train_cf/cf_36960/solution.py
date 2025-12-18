"""
QUESTION:
Write a function `main` that takes in command-line arguments for a Dataflow job and generates the necessary command to submit the job. The required arguments are project ID, runner type, staging location, temp location, number of workers, worker machine type, setup file path, region, and storage bucket. The function should format the command string with the provided arguments in the correct locations.
"""

import argparse

def main(project, runner, staging_location, temp_location, num_workers, worker_machine_type, setup_file, region, storage_bucket):
    command = f"""\
    --project {project} \
    --runner {runner} \
    --staging_location gs://{storage_bucket}/{staging_location} \
    --temp_location gs://{storage_bucket}/{temp_location} \
    --num_workers {num_workers} \
    --worker_machine_type {worker_machine_type} \
    --setup_file {setup_file} \
    --region {region} \
    --storage-bucket {storage_bucket} \
    """
    return command