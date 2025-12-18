"""
QUESTION:
Write a function named `get_open_files_and_sockets` that takes a process ID as input. Given a core dump file from a process with a file descriptor leak, the function should return a list of files and sockets that the process had opened before crashing. Note that the function may not be able to directly retrieve this information from the core dump file, and may need to use alternative methods such as checking the `/proc/<pid>/fd` directory or attaching a debugger.
"""

def get_open_files_and_sockets(pid):
    """
    Given a process ID, returns a list of files and sockets that the process had opened.
    
    This function relies on the /proc filesystem, typically found on Linux systems.
    The /proc filesystem provides a way to access information about the running process.
    
    Parameters:
    pid (int): The ID of the process.
    
    Returns:
    list: A list of files and sockets that the process had opened.
    """
    
    # Import the os module to interact with the operating system
    import os
    
    # Construct the path to the /proc filesystem for the given process ID
    proc_dir = f"/proc/{pid}/fd"
    
    # Initialize an empty list to store the open files and sockets
    open_files_and_sockets = []
    
    # Check if the /proc filesystem directory exists for the given process ID
    if os.path.exists(proc_dir):
        # Iterate over each file descriptor in the /proc filesystem directory
        for fd in os.listdir(proc_dir):
            # Construct the path to the file descriptor
            fd_path = os.path.join(proc_dir, fd)
            
            # Try to read the file descriptor as a symbolic link
            try:
                # Get the target of the symbolic link
                target = os.readlink(fd_path)
                
                # Add the target to the list of open files and sockets
                open_files_and_sockets.append(target)
            except OSError:
                # If the file descriptor is not a symbolic link, skip it
                continue
    
    # Return the list of open files and sockets
    return open_files_and_sockets