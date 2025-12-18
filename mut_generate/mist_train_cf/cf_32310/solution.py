"""
QUESTION:
Create a Python function `select_test_script` that takes two inputs: `sys_argv` (a list of command-line arguments) and `config` (a list of configuration variables). Based on the given conditions, the function should return the appropriate test script to call. The conditions are:
- If "msvc" is found in any of the command-line arguments in `sys_argv`, set the script to "alltests_msvc.bat".
- If "msvc" is not found, set the script to "alltests_gcc.bat".
- If the first element of `config` is "standalone_singleabi", prefix the script with "standalone_".
- If none of the above conditions are met, set the script to "test_all".
"""

def select_test_script(sys_argv, config):
    tocall = "alltests_msvc.bat" if "msvc" in sys_argv else "alltests_gcc.bat"
    if config and config[0] == "standalone_singleabi":
        tocall = "standalone_" + tocall
    return tocall