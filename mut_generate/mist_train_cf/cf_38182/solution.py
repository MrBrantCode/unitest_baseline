"""
QUESTION:
Create a function `get_architecture_info(architecture)` that takes a string `architecture` as input and returns a tuple containing the breakpoint opcodes and instructions specific to that architecture. If the architecture is not specified or is unsupported, the function should return an error message. The function should support the following architectures: x86_64, i386, arm, and aarch64, and return the corresponding breakpoint opcodes and instructions as follows: 
- For x86_64 and i386, return `(["int3"], [' mov', ' addl ', 'ret'])`.
- For arm and aarch64, return `(["brk", "udf"], [' add ', ' ldr ', ' str '])`.
"""

def get_architecture_info(architecture):
    if architecture in ["x86_64", 'i386']:
        return (["int3"], [' mov', ' addl ', 'ret'])
    elif architecture in ["arm", "aarch64"]:
        return (["brk", "udf"], [' add ', ' ldr ', ' str '])
    else:
        return "Unsupported architecture"