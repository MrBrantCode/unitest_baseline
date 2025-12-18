"""
QUESTION:
Write a function named `extract_ne_header` that takes a byte array representing the NE file header as input. The function should extract the following 13 fields from the byte array and return them in a suitable data structure:

- ne_segtab (unsigned 16-bit integer)
- ne_rsrctab (unsigned 16-bit integer)
- ne_restab (unsigned 16-bit integer)
- ne_modtab (unsigned 16-bit integer)
- ne_imptab (unsigned 16-bit integer)
- ne_nrestab (signed 32-bit integer)
- ne_cmovent (unsigned 16-bit integer)
- ne_align (unsigned 16-bit integer)
- ne_cres (unsigned 16-bit integer)
- ne_exetyp (single byte)
- ne_flagsothers (single byte)
- ne_pretthunks (unsigned 16-bit integer)
- ne_psegrefbytes (unsigned 16-bit integer)

Assume the input byte array is well-formed and contains sufficient data to extract all required fields.
"""

def extract_ne_header(byte_array):
    ne_segtab = int.from_bytes(byte_array[0:2], byteorder='little')
    ne_rsrctab = int.from_bytes(byte_array[2:4], byteorder='little')
    ne_restab = int.from_bytes(byte_array[4:6], byteorder='little')
    ne_modtab = int.from_bytes(byte_array[6:8], byteorder='little')
    ne_imptab = int.from_bytes(byte_array[8:10], byteorder='little')
    ne_nrestab = int.from_bytes(byte_array[10:14], byteorder='little', signed=True)
    ne_cmovent = int.from_bytes(byte_array[14:16], byteorder='little')
    ne_align = int.from_bytes(byte_array[16:18], byteorder='little')
    ne_cres = int.from_bytes(byte_array[18:20], byteorder='little')
    ne_exetyp = byte_array[20]
    ne_flagsothers = byte_array[21]
    ne_pretthunks = int.from_bytes(byte_array[22:24], byteorder='little')
    ne_psegrefbytes = int.from_bytes(byte_array[24:26], byteorder='little')

    return {
        "ne_segtab": ne_segtab,
        "ne_rsrctab": ne_rsrctab,
        "ne_restab": ne_restab,
        "ne_modtab": ne_modtab,
        "ne_imptab": ne_imptab,
        "ne_nrestab": ne_nrestab,
        "ne_cmovent": ne_cmovent,
        "ne_align": ne_align,
        "ne_cres": ne_cres,
        "ne_exetyp": ne_exetyp,
        "ne_flagsothers": ne_flagsothers,
        "ne_pretthunks": ne_pretthunks,
        "ne_psegrefbytes": ne_psegrefbytes
    }