"""
QUESTION:
Implement a function `decode(status)` that takes an integer status and decodes it into its high byte (exit status) and low byte (signal number). The function should return a tuple containing the exit status and signal number, where the high bit of the low byte is set if a core file was produced.
"""

def decode(status):
    """
    Decodes an integer status into its high byte (exit status) and low byte (signal number).
    
    Args:
        status (int): The status to be decoded.
    
    Returns:
        tuple: A tuple containing the exit status and signal number.
    """
    signum = status & 0xFF
    exitstatus = (status & 0xFF00) >> 8
    return (exitstatus, signum)