"""
QUESTION:
Implement a function named `get_mounts` that takes a string mode as input and returns a list of `Mount` objects. The function should return different lists of mounts based on the mode, which can be 'local', 'docker', or 'ec2'. The mounts consist of code mounts, data mounts, and output mounts. The function should define the path, mount_point, and output for each mount type based on the given mode.
"""

from typing import List

class Mount:
    def __init__(self, mount_type: str, path: str, mount_point: str, output: bool):
        self.mount_type = mount_type
        self.path = path
        self.mount_point = mount_point
        self.output = output

def get_mounts(mode: str) -> List[Mount]:
    LOCAL_OUTPUT_DIR = '/local/output'
    REMOTE_OUTPUT_DIR = '/remote/output'
    code_mounts = [Mount('code', '/local/code', '/remote/code', False)]
    data_mounts = [Mount('data', '/local/data', '/remote/data', False)]

    if mode == 'local':
        output_mounts = [Mount('local', LOCAL_OUTPUT_DIR, REMOTE_OUTPUT_DIR, True)]
    elif mode == 'docker':
        output_dir = '/local/output/docker/'
        output_mounts = [Mount('local', output_dir, REMOTE_OUTPUT_DIR, True)]
    elif mode == 'ec2':
        output_mounts = [Mount('s3', 'data', REMOTE_OUTPUT_DIR, True)]

    mounts = code_mounts + data_mounts + output_mounts
    return mounts