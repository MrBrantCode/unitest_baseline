"""
QUESTION:
Implement a function `calculate_shard_limit(args)` that takes an `args` object containing `maxsize`, `maxcount`, and `debug` properties, and returns the limit on the number of samples for each shard. The function should enforce the following constraints: `maxsize` must be greater than 10,000,000 bytes and `maxcount` must be less than 1,000,000 samples. If the `debug` flag is True, the limit should be set to 200; otherwise, it should be set to positive infinity. If the constraints are not met, the function should return 0.
"""

import numpy as np

def calculate_shard_limit(args) -> int:
    if args.maxsize > 10000000 and args.maxcount < 1000000:
        limit_num_samples = 200 if args.debug else np.inf
        return limit_num_samples
    else:
        return 0