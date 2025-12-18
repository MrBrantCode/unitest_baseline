"""
QUESTION:
Implement a function `merge_capacity_commitments` that takes in a string `parent` representing the parent resource in the format "projects/myproject/locations/us" and a sequence of strings `capacity_commitment_ids` representing the IDs of capacity commitments to merge. The function should return a message indicating the success or failure of the merge operation, assuming all capacity commitments exist under the specified admin project and location. The function signature is `def merge_capacity_commitments(parent: str, capacity_commitment_ids: List[str]) -> str`.
"""

from typing import List

def merge_capacity_commitments(parent: str, capacity_commitment_ids: List[str]) -> str:
    # Perform the merge operation using the parent and capacity_commitment_ids
    # Assume the merge operation is performed successfully
    return "Capacity commitments merged successfully under the specified parent resource."