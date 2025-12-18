"""
QUESTION:
Construct a file path based on environment variables and conditions. Implement the function `construct_file_path()` that takes in three parameters: `AS_ROOT_CERT_FILENAME`, `AS_ROOT_CA_CERT_PATH`, and `is_enclave_info`. 

The function should construct the file path as follows:
- If `is_enclave_info` is `True`, use the `TEACLAVE_PROJECT_ROOT` environment variable and append "/release/tests/enclave_info.toml".
- If `is_enclave_info` is `False`, use the provided `AS_ROOT_CA_CERT_PATH`. If `AS_ROOT_CA_CERT_PATH` is not defined, set it to "../../keys/" + `AS_ROOT_CERT_FILENAME`. 

Note that the function should handle both Windows and Unix-like operating systems.
"""

import os

def construct_file_path(AS_ROOT_CERT_FILENAME, AS_ROOT_CA_CERT_PATH, is_enclave_info):
    if is_enclave_info:
        return os.path.join(os.environ.get('TEACLAVE_PROJECT_ROOT', ''), "release", "tests", "enclave_info.toml")
    else:
        if not AS_ROOT_CA_CERT_PATH:
            AS_ROOT_CA_CERT_PATH = os.path.join("..\..", "keys", AS_ROOT_CERT_FILENAME)
        return AS_ROOT_CA_CERT_PATH