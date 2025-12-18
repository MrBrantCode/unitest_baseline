"""
QUESTION:
Write a Python function `run_data_uploading_process(config_file_path: str) -> bool` that takes the path to a configuration file as input and returns a boolean value indicating whether the data uploading process should be executed based on the presence of `datasetId`, `datasetVersion`, or `datasetVersionEdition` settings in the `[dataUploader]` section of the configuration file. If any of these settings are present, return `False`; otherwise, return `True`.
"""

import configparser

def run_data_uploading_process(config_file_path: str) -> bool:
    config = configparser.ConfigParser()
    config.read(config_file_path)

    data_uploader_settings = config['dataUploader']
    relevant_settings = ['datasetId', 'datasetVersion', 'datasetVersionEdition']

    for setting in relevant_settings:
        if setting in data_uploader_settings:
            return False

    return True