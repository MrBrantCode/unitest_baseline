"""
QUESTION:
Implement a function `build_mpi_command` that takes the following parameters: `num_cores`, `script_name`, `host`, `port`, `last_stage`, `verbose`, and an optional `gui_port`. The function should construct and return an MPI command string that includes the specified number of cores, script name, hostname, port number, last stage, verbose flag, and GUI port (if provided). The command string should be in the format:
```
mpirun --map-by core --bind-to core -np {num_cores} python {script_name} --host {host} --port {port} --last_stage {last_stage} [options]
```
"""

def build_mpi_command(num_cores, script_name, host, port, last_stage, verbose, gui_port=None):
    mpi_command = f"mpirun --map-by core --bind-to core -np {num_cores} python {script_name} --host {host} --port {port} --last_stage {last_stage}"
    if verbose:
        mpi_command += " --verbose"
    if gui_port:
        mpi_command += f" --gui_port {gui_port}"
    return mpi_command