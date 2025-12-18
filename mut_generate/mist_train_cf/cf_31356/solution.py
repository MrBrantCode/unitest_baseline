"""
QUESTION:
Write a function `generate_output_files` that takes the following parameters:
- `colour_corrections` (list of strings): A list of colour correction methods.
- `distortion_corrections` (list of strings): A list of distortion correction methods.
- `rescalings` (list of strings): A list of rescaling methods.
- `numerical_range` (int): The range of numerical identifiers.

The function should return a list of unique output file names based on all possible combinations of the correction methods and numerical identifiers. Each output file name is constructed by combining the colour correction, distortion correction, rescaling, and numerical identifier with hyphens.
"""

def generate_output_files(colour_corrections, distortion_corrections, rescalings, numerical_range):
    output_files = []
    for cc in colour_corrections:
        for dc in distortion_corrections:
            for rs in rescalings:
                for n in range(numerical_range):
                    output_files.append('-'.join([cc, dc, rs, str(n)]))
    return output_files