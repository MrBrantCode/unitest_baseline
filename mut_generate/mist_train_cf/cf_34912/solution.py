"""
QUESTION:
Implement the `get_transformers` function and the `Transformer` class. The `get_transformers` function should return a list of Transformer instances along with their corresponding metadata based on the provided scan mode. The `Transformer` class should have a `run` method that simulates the data transformation process. The `run` method should accept a `request_meta` parameter, which represents the metadata associated with the data transformation task. The `Transformer` instances should be executed concurrently using asyncio.

The `get_transformers` function should return a list of tuples, where each tuple contains a Transformer instance and its corresponding metadata. The `Transformer` class should have an `async run` method, which means it can be awaited.

Restrictions: The solution must use asyncio for concurrency. The `get_transformers` function should return a list of Transformer instances and their corresponding metadata. The `Transformer` class should have an `async run` method.
"""

import asyncio

class Transformer:
    async def run(self, request_meta):
        # Simulate data transformation process
        print(f"Running data transformation for {request_meta}...")
        await asyncio.sleep(1)  # Simulate asynchronous data processing
        print(f"Data transformation completed for {request_meta}")

def get_transformers(scan_mode):
    # Return a list of Transformer instances and their corresponding metadata based on the scan mode
    if scan_mode == 'mode1':
        return [(Transformer(), 'metadata1'), (Transformer(), 'metadata2')]
    elif scan_mode == 'mode2':
        return [(Transformer(), 'metadata3'), (Transformer(), 'metadata4')]
    else:
        return []