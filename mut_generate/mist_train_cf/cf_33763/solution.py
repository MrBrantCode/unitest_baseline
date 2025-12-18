"""
QUESTION:
Implement a function `substitute(target_relpath)` that takes a string `target_relpath` representing a Python package distribution wheel file path in the format `{distribution_name}-{version}-{python_tag}-{abi_tag}-{platform_tag}.whl`. 

The function should extract the `wheel_distribution_name`, `package_version`, `python_tag`, `abi_tag`, and `platform_tag` from the file path, check if the `wheel_distribution_name` starts with 'datadog_', and return a tuple containing the `wheel_distribution_name` and `package_version` if `wheel_distribution_name` is not in the set `EXCEPTIONS = {'datadog_checks_base', 'datadog_checks_dev', 'datadog_checks_downloader'}`. If `wheel_distribution_name` is in `EXCEPTIONS`, return the string "EXCEPTION". If `wheel_distribution_name` does not start with 'datadog_', raise an assertion error.
"""

import os.path

from pkg_resources import safe_name

EXCEPTIONS = {'datadog_checks_base', 'datadog_checks_dev', 'datadog_checks_downloader'}


def substitute(target_relpath):
    filename = os.path.basename(target_relpath)
    name, ext = os.path.splitext(filename)
    wheel_distribution_name, package_version, python_tag, abi_tag, platform_tag = name.split('-')
    assert wheel_distribution_name.startswith('datadog_'), wheel_distribution_name
    if wheel_distribution_name in EXCEPTIONS:
        return "EXCEPTION"
    else:
        return (wheel_distribution_name, package_version)