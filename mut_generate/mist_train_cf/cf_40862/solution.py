"""
QUESTION:
Write a function `getRegisterName(mnemonic)` that takes a string `mnemonic` as input and returns the corresponding x86 register name based on the following mappings:

- "mov_b" returns "al"
- "mov_w" returns "ax"
- "mov_l" returns "eax"
- "mov_q" returns "rax"
- "add_b" returns "cl"
- "add_w" returns "cx"
- "add_l" returns "ecx"
- "add_q" returns "rcx"
- "sub_b" returns "dl"
- "sub_w" returns "dx"
- "sub_l" returns "edx"
- "sub_q" returns "rdx"

If the input mnemonic is not found in the mapping, the function should return "Invalid mnemonic".
"""

def entrance(mnemonic):
    mapping = {
        "mov_b": "al",
        "mov_w": "ax",
        "mov_l": "eax",
        "mov_q": "rax",
        "add_b": "cl",
        "add_w": "cx",
        "add_l": "ecx",
        "add_q": "rcx",
        "sub_b": "dl",
        "sub_w": "dx",
        "sub_l": "edx",
        "sub_q": "rdx"
    }
    return mapping.get(mnemonic, "Invalid mnemonic")