"""
QUESTION:
Write a function named `generate_zip_commands` that takes a version number as a string parameter and returns two strings representing the commands to zip the Linux and macOS files using the `cross-zip` tool. The version number should be inserted into the naming convention `dwebx-$VERSION-linux-x64` and `dwebx-$VERSION-macos-x64` for the input files, and `dwebx-$VERSION-linux-x64.zip` and `dwebx-$VERSION-macos-x64.zip` for the output files. The `cross-zip` tool is assumed to be installed and available at the path `../node_modules/.bin/cross-zip`.
"""

def generate_zip_commands(version):
    linux_command = f"../node_modules/.bin/cross-zip dwebx-{version}-linux-x64 ../dist/dwebx-{version}-linux-x64.zip"
    macos_command = f"../node_modules/.bin/cross-zip dwebx-{version}-macos-x64 ../dist/dwebx-{version}-macos-x64.zip"
    return linux_command, macos_command