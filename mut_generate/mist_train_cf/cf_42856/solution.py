"""
QUESTION:
Implement a function `parse_directive` that handles parsing logic for the following assembly language directives: `.entry`, `.align`, `.db`, and `.zero`. 

The function should take a string `line` as input, which represents a single line of assembly code containing one of the supported directives. The function should parse the directive and its corresponding value(s) and perform the required actions.

The function should support the following directives:
- `.entry <value>`: Parse the `<value>` and return the parsed immediate value.
- `.align <value>`: Align the current section to the specified alignment `<value>`.
- `.db <data>`: Write the specified byte data to the current section. The `<data>` can be a comma-separated list of byte values in hexadecimal format.
- `.zero <size>`: Reserve a block of zero-initialized memory of the specified `<size>`.

Assume that the function has access to a `current_section` object with methods `align`, `write`, and `reserve_zero` to perform the necessary actions for each directive. Also, assume that the function has a `try_parse_imm` method to parse immediate values.
"""

def parseDirective(line, current_section):
    """
    Parse assembly language directives.

    Args:
    line (str): A single line of assembly code containing one of the supported directives.
    current_section (object): An object with methods align, write, and reserve_zero.

    Returns:
    int: The parsed immediate value for the .entry directive.
    """
    if line.startswith('.entry'):
        entry = line.split()[1]
        return int(entry, 0)  # parse immediate value with base detection
    elif line.startswith('.align'):
        current_section.align(int(line.split()[1]))
    elif line.startswith('.db'):
        data = line[3:].split(',')
        bytes_data = bytes(int(i.strip(), 16) for i in data)
        current_section.write(bytes_data)
    elif line.startswith('.zero'):
        data = line[5:].strip()
        if data.startswith('0x'):
            n = int(data, 16)
        else:
            n = int(data)
        current_section.reserve_zero(n)