"""
QUESTION:
Create a function `generate_setup_script` that takes a string `target_platform` as input and returns a string of shell commands for setting up a development environment. The `target_platform` can be "linux", "macos", or "windows". For "linux", the setup script should install the required Rust target. For "macos", it should upgrade pip and virtualenv. For "windows", it should install the Chocolatey package manager. If the `target_platform` is not one of the supported platforms, the function should return "Unsupported platform".
"""

def generate_setup_script(target_platform: str) -> str:
    if target_platform == "linux":
        return "rustup target add $TARGET"
    elif target_platform == "macos":
        return "sudo pip install --upgrade pip\nsudo pip install virtualenv --upgrade"
    elif target_platform == "windows":
        return "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    else:
        return "Unsupported platform"