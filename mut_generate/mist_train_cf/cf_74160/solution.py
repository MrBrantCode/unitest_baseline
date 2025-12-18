"""
QUESTION:
Implement a function `mono_platform_invoke` that demonstrates the usage of Platform Invoke (P/Invoke) in Mono on Linux and Solaris. The function should load a native library, connect to a specified function in the library, and call the function. The function name should be provided as a string, and the function should be callable from managed code.
"""

import ctypes

def mono_platform_invoke(lib_name, func_name):
    """
    Demonstrates the usage of Platform Invoke (P/Invoke) in Mono on Linux and Solaris.
    
    Args:
        lib_name (str): The name of the native library to load.
        func_name (str): The name of the function to call in the library.
    
    Returns:
        The result of the function call.
    """
    # Load the native library
    lib = ctypes.CDLL(lib_name)
    
    # Get the function from the library
    func = getattr(lib, func_name)
    
    # Call the function
    return func()