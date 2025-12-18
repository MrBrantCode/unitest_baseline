"""
QUESTION:
Implement the function `performQuaternionOperation` that takes in two quaternions `q1` and `q2`, and a string `operation`. The function should perform the specified operation on the given quaternions and return the result.

The function should take two lists of 4 floats representing the quaternions (w, x, y, z) and a string representing the operation. The operation string can be one of the following: "add", "subtract", "multiply", or "conjugate".

For "conjugate" operation, only `q1` is required, and `q2` can be an empty list. 

The function should support the following operations:
- "add": Add the two quaternions together.
- "subtract": Subtract the second quaternion from the first.
- "multiply": Multiply the two quaternions together.
- "conjugate": Compute the conjugate of the given quaternion.
"""

from typing import List

def performQuaternionOperation(q1: List[float], q2: List[float], operation: str) -> List[float]:
    if operation == "add":
        return [q1[0] + q2[0], q1[1] + q2[1], q1[2] + q2[2], q1[3] + q2[3]]
    elif operation == "subtract":
        return [q1[0] - q2[0], q1[1] - q2[1], q1[2] - q2[2], q1[3] - q2[3]]
    elif operation == "multiply":
        w = q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3]
        x = q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2]
        y = q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1]
        z = q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]
        return [w, x, y, z]
    elif operation == "conjugate":
        return [q1[0], -q1[1], -q1[2], -q1[3]]