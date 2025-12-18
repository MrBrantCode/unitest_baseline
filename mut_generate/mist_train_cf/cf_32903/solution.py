"""
QUESTION:
Implement a function `configure_parser` that extends an existing argument parser with new options for specifying the partitioning strategy and its associated arguments. The function should add two new options: `--partition` with a default value of 'iid' and valid choices of 'iid', 'dirichlet', and 'power-law', and `--partition_args` for additional arguments specific to the chosen partitioning strategy. The existing options should remain unchanged.
"""

import argparse

def configure_parser(parser):
    """
    Extends an existing argument parser with new options for specifying the partitioning strategy and its associated arguments.

    Args:
    parser (argparse.ArgumentParser): The existing argument parser.

    Returns:
    argparse.ArgumentParser: The extended argument parser.
    """
    parser.add_argument('--partition',
                        type=str,
                        default='iid',
                        choices=['iid', 'dirichlet', 'power-law'],
                        help='How to split the dataset into different parts. Only be used with not federated dataset, such as mnist.')
    parser.add_argument('--partition_args',
                        type=str,
                        help='Additional arguments specific to the chosen partitioning strategy.')
    return parser