"""
QUESTION:
You are given a tuple of file paths ('foo', 'sub/foo', 'sub/foo.c') and a list or tuple `vartpl` containing file extensions. Write a function `get_final_varfiles` that takes `vartpl` as an input, iterates over the given file paths, appends the corresponding file extension from `vartpl` to each file path, and returns the final values of `varfile` after the loop completes. Assume the file extensions in `vartpl` match the order of their appearance in the file structure and are in the format of 'j2', 'json', etc.
"""

def get_final_varfiles(vartpl):
    file_paths = ('foo', 'sub/foo', 'sub/foo.c')
    varfiles = []
    
    for i, path in enumerate(file_paths):
        varfile = f"{path}.{vartpl[i]}"
        varfiles.append(varfile)
        
    return varfiles