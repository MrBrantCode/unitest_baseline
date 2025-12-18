"""
QUESTION:
Implement a function `parseVertexShader(vertexShaderSource)` that takes a string representing a vertex shader source code in GLSL syntax as input and returns a dictionary where the keys are the variable names and the values are their corresponding data types. The input variable declarations should be in the format `layout (location = X) in data_type variable_name;` where data_type is the type of the variable and variable_name is the name of the variable.
"""

import re

def parseVertexShader(vertexShaderSource):
    variable_pattern = r'layout\s*\(\s*location\s*=\s*\d+\s*\)\s*in\s+(\w+)\s+(\w+);'
    variable_matches = re.findall(variable_pattern, vertexShaderSource)
    variable_dict = {name: data_type for data_type, name in variable_matches}
    return variable_dict