"""
QUESTION:
Set a conditional breakpoint in a GDB program based on the value of a global variable, without associating it with any source code line. The function should take the variable name and the target value as inputs and trigger the breakpoint when the variable's value equals the target value.
"""

def set_breakpoint(var_name, target_value):
    return f"break if {var_name} == {target_value}"