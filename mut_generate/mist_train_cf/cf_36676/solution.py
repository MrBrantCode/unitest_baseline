"""
QUESTION:
Write a function `parse_helm_install_command(command)` that takes a string `command` as input, representing a Helm install command, and returns a dictionary containing the configuration settings specified using the `--set` flag. The `--set` flag is in the format `--set key=value`, where `key` and `value` may contain spaces and special characters. The function should return a dictionary where the keys are the configuration keys and the values are the corresponding configuration values.
"""

import re

def parse_helm_install_command(command):
    set_flags = re.findall(r'--set\s+(\S+)=([\S\s]+?)(?=\s+--set|\s*$)', command)
    config_settings = {}
    for flag in set_flags:
        key = flag[0]
        value = flag[1].strip()
        config_settings[key] = value
    return config_settings