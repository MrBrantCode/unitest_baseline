"""
QUESTION:
Write a function `process_command_line_argument` that takes a string representing a command-line argument as input. The command consists of the path to an executable program, an action, an account identifier, and an optional `--dry-run` flag. Extract the path to the executable program, the action, the account identifier, and the presence of the `--dry-run` flag. Process the extracted information accordingly based on the presence of the `--dry-run` flag. The function should return a dictionary containing the extracted information.
"""

import argparse

def process_command_line_argument(command):
    parser = argparse.ArgumentParser()
    parser.add_argument('executable_path', help='Path to the executable program')
    parser.add_argument('action', help='Action to be performed')
    parser.add_argument('account_identifier', help='Account identifier or account number')
    parser.add_argument('--dry-run', action='store_true', help='Simulate the action without making actual changes')

    args = parser.parse_args(command.split()[1:])  # Splitting the command and excluding the program name
    extracted_info = {
        'executable_path': args.executable_path,
        'action': args.action,
        'account_identifier': args.account_identifier,
        'dry_run': args.dry_run
    }

    # Process the extracted information based on the presence of the --dry-run flag
    if args.dry_run:
        print("Simulating the action without making actual changes")
        # Add logic for simulation here
    else:
        print("Performing the action")

    return extracted_info