"""
QUESTION:
Create a function `generate_rsync_command` that generates a command for synchronizing files and directories using the `rsync` utility. The function should take in a source path `from_path`, a destination path `to_path`, and an optional flag `relative` for relative synchronization. The generated command should include options for deleting extraneous files from the destination, displaying overall progress, preserving timestamps, and optionally using relative paths. The function should return a string representing the complete `rsync` command. The `relative` flag is False by default.
"""

def generate_rsync_command(from_path: str, to_path: str, relative: bool = False) -> str:
    cmd = [
        "rsync",
        "--delete",
        "--info=progress2",
        "--times",
        from_path,
        to_path
    ]
    if relative:
        cmd.append("--relative")
    
    return " ".join(cmd)