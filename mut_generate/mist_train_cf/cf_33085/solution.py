"""
QUESTION:
Write a function named `parse_arguments` that takes a list of command-line arguments and returns a dictionary containing the parsed options and their values. The options include:
- `target` or `t`: a string specifying the target IP address or domain name.
- `threads` or `r`: an integer specifying the number of threads, defaulting to 256 if not provided.
- `port` or `p`: an integer specifying the web server port, defaulting to 80 if not provided.
- `tor` or `T`: a boolean indicating whether to anonymize through Tor, defaulting to False.
- `help` or `h`: a boolean indicating whether to display the help message, defaulting to False.

The function should process the list of arguments, updating the corresponding values in the dictionary. If an option requires a value, it should be retrieved from the next argument in the list.
"""

from typing import List, Dict, Union

def parse_arguments(args: List[str]) -> Dict[str, Union[str, int, bool]]:
    options = {'target': '', 'threads': 256, 'port': 80, 'tor': False, 'help': False}
    i = 0
    while i < len(args):
        if args[i] in ['-t', '--target']:
            options['target'] = args[i + 1]
            i += 2
        elif args[i] in ['-r', '--threads']:
            options['threads'] = int(args[i + 1])
            i += 2
        elif args[i] in ['-p', '--port']:
            options['port'] = int(args[i + 1])
            i += 2
        elif args[i] in ['-T', '--tor']:
            options['tor'] = True
            i += 1
        elif args[i] in ['-h', '--help']:
            options['help'] = True
            break
        else:
            i += 1
    return options