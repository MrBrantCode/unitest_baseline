"""
QUESTION:
Create a function `create_new_macho_section` that takes in the following parameters: `new_segment`, `vmaddr`, `INJECTION_SECTION_NAME`, `is_64_bit`, `section_64`, and `section`. The function should create a new Mach-O section based on the provided specifications, handling both 32-bit and 64-bit Mach-O files. The new section's properties should be set as follows: `sectname` to `INJECTION_SECTION_NAME`, `segname` to `new_segment.segname`, `addr` to `vmaddr`, `size` to 0, and `offset` to `new_segment.fileoff`. The function should return the newly created section object.
"""

def create_new_macho_section(new_segment, vmaddr, INJECTION_SECTION_NAME, is_64_bit, section_64, section):
    new_section = section_64() if is_64_bit else section()
    new_section.sectname = INJECTION_SECTION_NAME
    new_section.segname = new_segment.segname
    new_section.addr = vmaddr
    new_section.size = 0
    new_section.offset = new_segment.fileoff
    return new_section