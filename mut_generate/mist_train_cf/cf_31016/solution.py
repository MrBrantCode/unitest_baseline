"""
QUESTION:
Implement a function `get_exported_source_file_name` that takes command-line arguments as input and returns the name of the exported source file. The function should accept the `-o` option to specify the output file name. If the `-o` option is provided with a file name, it should return the specified file name. If only `-o` is provided without a file name, or if no `-o` option is provided, it should return the default output file name by replacing the extension of the first command-line argument (input file name) with `.cpp`.
"""

import argparse
import os

def get_exported_source_file_name(args):
    parser = argparse.ArgumentParser(description='Process command-line arguments')
    parser.add_argument('-o', dest='output_file', help='Name of the exported source file')
    parsed_args = parser.parse_args(args)

    if parsed_args.output_file:
        return parsed_args.output_file
    else:
        input_file_name, input_file_ext = os.path.splitext(args[0])
        return input_file_name + '.cpp'