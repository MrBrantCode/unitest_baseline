"""
QUESTION:
Create a function called `param_file` that generates a MOOG parameter file. The function should accept the following parameters: 

- `linelist` (string): a string representing the linelist file
- `atmosphere` (int, default 0): an integer representing the atmosphere type
- `molecules` (int, default 1): an integer representing the molecules type
- `lines` (int, default 0): an integer representing the lines type
- `flux` (int, default 0): an integer representing the flux type
- `damp` (int, default 0): an integer representing the damp type
- `plot` (int, default 0): an integer representing the plot type
- `units` (int, default 0): an integer representing the units type
- `verbose` (bool, default False): a boolean indicating whether to display the parameter file on the screen

The function should return the parameter file as a string if `verbose` is False. If `verbose` is True, the function should print the parameter file to the screen instead of returning it. The parameter file format should follow the MOOG parameter file format, with each parameter on a new line, followed by its corresponding value.
"""

def param_file(linelist, atmosphere=0, molecules=1, lines=0, flux=0, damp=0, plot=0, units=0, verbose=False):
    param_file_content = f"{linelist}\n"
    param_file_content += f"atmosphere      {atmosphere}\n"
    param_file_content += f"molecules       {molecules}\n"
    param_file_content += f"lines           {lines}\n"
    param_file_content += f"flux            {flux}\n"
    param_file_content += f"damp            {damp}\n"
    param_file_content += f"plot            {plot}\n"
    param_file_content += f"units           {units}\n"

    if verbose:
        print(param_file_content)
    else:
        return param_file_content