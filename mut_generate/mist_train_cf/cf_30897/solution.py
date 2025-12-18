"""
QUESTION:
Implement the `parse_args` function to parse command-line arguments using the `argparse` module. The function should accept the following arguments:

- `--config` or `-c`: a string representing the path to the configuration file, defaulting to 'config.ini'.
- `--length` or `-n`: an integer representing the length of the generated text, defaulting to 100.
- `--last` or `-l`: an optional integer representing the Markov Last parameter, overriding the value in the configuration file if provided.
- `command`: a positional argument representing the command to be executed, with valid choices limited to 'help', 'learn', 'say', 'tweet', 'generate', and 'scrape'.
"""

import argparse

def parse_args(argv=None):
    root = argparse.ArgumentParser()
    root.add_argument('--config', '-c', default='config.ini')
    root.add_argument('--length', '-n', default=100, type=int)
    root.add_argument('--last', '-l', type=int, help='Markov Last param. Default: use config.')
    root.add_argument('command', choices=('help', 'learn', 'say', 'tweet', 'generate', 'scrape'))
    return root.parse_args(argv)