"""
QUESTION:
Write a function `generate_upgrade_commands` that takes a list of package names and a target version as input, and returns a list of `apt-get` commands to upgrade each package to the specified version. The commands should be in the format "sudo apt-get install --only-upgrade <package_name>=<target_version> -y".
"""

def generate_upgrade_commands(package_names, target_version):
    upgrade_commands = []
    for package in package_names:
        command = f"sudo apt-get install --only-upgrade {package}={target_version} -y"
        upgrade_commands.append(command)
    return upgrade_commands