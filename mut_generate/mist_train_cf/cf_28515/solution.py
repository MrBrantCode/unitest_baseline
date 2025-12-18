"""
QUESTION:
Implement a function named `parse_command_line_arguments` that takes command-line arguments as input and returns a dictionary containing the extracted configuration parameters for a machine learning model training process. The function should accept the following command-line arguments: 
- `--batch_size <value>`: Specifies the batch size for training, which is an integer.
- `--sample_ratio <value>`: Specifies the sample ratio for data sampling, which is a float.
- `--workers <value>`: Specifies the number of workers for data loading, which is an integer.
- `--print_freq <value>`: Specifies the frequency for printing training progress, which is an integer.
- `--distributed`: Indicates that distributed training will be used, which is a boolean flag.
- `--world_size <value>`: Specifies the total number of GPUs to be used for distributed training, which is an integer.
- `--dist_url <value>`: Specifies the URL for setting up the distributed training environment, which is a string.
- `--use_apex`: Indicates the use of the Apex library for mixed precision training, which is a boolean flag.
- `--sync_param`: Indicates the synchronization of parameters during training, which is a boolean flag.

The returned dictionary should contain the corresponding keys for each command-line argument.
"""

import argparse

def parse_command_line_arguments(args):
    parser = argparse.ArgumentParser(description='Distributed Training Script Argument Parser')
    parser.add_argument('--batch_size', type=int, help='Batch size for training')
    parser.add_argument('--sample_ratio', type=float, help='Sample ratio for data sampling')
    parser.add_argument('--workers', type=int, help='Number of workers for data loading')
    parser.add_argument('--print_freq', type=int, help='Frequency for printing training progress')
    parser.add_argument('--distributed', action='store_true', help='Use distributed training')
    parser.add_argument('--world_size', type=int, help='Total number of GPUs for distributed training')
    parser.add_argument('--dist_url', type=str, help='URL for setting up distributed training environment')
    parser.add_argument('--use_apex', action='store_true', help='Use Apex library for mixed precision training')
    parser.add_argument('--sync_param', action='store_true', help='Synchronize parameters during training')

    parsed_args = parser.parse_args(args)

    return {
        'batch_size': parsed_args.batch_size,
        'sample_ratio': parsed_args.sample_ratio,
        'workers': parsed_args.workers,
        'print_freq': parsed_args.print_freq,
        'distributed': parsed_args.distributed,
        'world_size': parsed_args.world_size,
        'dist_url': parsed_args.dist_url,
        'use_apex': parsed_args.use_apex,
        'sync_param': parsed_args.sync_param
    }