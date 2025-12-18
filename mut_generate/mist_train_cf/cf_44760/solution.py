"""
QUESTION:
Write a function called `requires_restart` that determines if the installation of .NET Framework 3.5 SP1 requires a restart of the machine. The function should take into account whether other updates are being installed concurrently and whether those updates require a restart.
"""

def requires_restart(other_updates, requires_restart):
    """
    Determines if the installation of .NET Framework 3.5 SP1 requires a restart of the machine.
    
    Args:
        other_updates (bool): Whether other updates are being installed concurrently.
        requires_restart (bool): Whether other updates require a restart.

    Returns:
        bool: Whether a restart is required after installation.
    """
    return other_updates and requires_restart