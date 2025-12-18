"""
QUESTION:
Implement a function named `parse_args` that uses the `argparse` module to parse command-line arguments. The function should support the following options:

- `--port` or `-p`: an integer value representing the port on which the web server should listen.
- `--config-file` or `-c`: a string value representing the path to the configuration file for the web server.
- `--debug` or `-d`: a boolean value that enables debug mode.

The function should provide appropriate help messages for each option and return the parsed arguments.
"""

import argparse

def parse_args(argv):
    ap = argparse.ArgumentParser(description='home automation web server')
    ap.add_argument('--debug', '-d', action='store_true', help='debug mode; log to stdout, disable all external comm')
    ap.add_argument('--port', '-p', type=int, help='port on which the web server should listen')
    ap.add_argument('--config-file', '-c', type=str, help='path to the configuration file for the web server')
    return ap.parse_args(argv)