"""
QUESTION:
Implement a Python function named `get_gdb` that accepts the following parameters: `oocd_args`, `ip`, `log_level`, `log_stream_handler`, `log_file_handler`, and `**kwargs`. This function should return a dictionary containing the redefined GDB settings based on the provided parameters. Each parameter should be included in the dictionary only if its value is not `None`. The function should also handle any additional keyword arguments.
"""

def get_gdb(oocd_args=None, ip=None, log_level=None, log_stream_handler=None, log_file_handler=None, **kwargs):
    gdb_settings = {}

    if oocd_args is not None:
        gdb_settings['oocd_args'] = oocd_args
    if ip is not None:
        gdb_settings['ip'] = ip
    if log_level is not None:
        gdb_settings['log_level'] = log_level
    if log_stream_handler is not None:
        gdb_settings['log_stream_handler'] = log_stream_handler
    if log_file_handler is not None:
        gdb_settings['log_file_handler'] = log_file_handler

    # Handle additional keyword arguments
    for key, value in kwargs.items():
        gdb_settings[key] = value

    return gdb_settings