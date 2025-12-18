"""
QUESTION:
Create a function `check_numpy_version` that takes a string `current_version` representing the current version of `numpy` as input, where `current_version` is in the format "x.y.z" (x, y, and z are integers representing the major, minor, and micro versions respectively). The function should return a string representing the command needed to install a version less than 1.22 if the current version is greater than or equal to 1.22, otherwise return "No installation needed". The returned command should be in the format "pip install numpy==x.y.z" where x, y, and z are the major, minor, and micro versions of the required `numpy` version.
"""

def check_numpy_version(current_version: str) -> str:
    np_version = current_version.split('.')
    np_major, np_minor = [int(v) for v in np_version][:2]
    if np_major >= 1 and np_minor >= 22:
        required_version = f"{np_major}.{np_minor - 1}.0"
        return f"pip install numpy=={required_version}"
    else:
        return "No installation needed"