"""
QUESTION:
Create a function named `add_ddp_arguments` that takes an `argparse.ArgumentParser` object as input. The function should add a group of arguments titled "DDP arguments" to the parser with the following arguments: 
- `--ddp.disable`: a boolean argument of type `store_true` indicating whether DDP should be disabled.
- `--ddp.rank`: an integer argument with a default value of 0, representing the node rank for distributed training.
- `--ddp.world-size`: an integer argument with a default value of -1, representing the world size for DDP. The function should return the modified parser.
"""

import argparse

def add_ddp_arguments(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    group = parser.add_argument_group(
        title="DDP arguments", description="DDP arguments"
    )
    group.add_argument("--ddp.disable", action="store_true", help="Don't use DDP")
    group.add_argument(
        "--ddp.rank", type=int, default=0, help="Node rank for distributed training"
    )
    group.add_argument(
        "--ddp.world-size", type=int, default=-1, help="World size for DDP"
    )
    return parser