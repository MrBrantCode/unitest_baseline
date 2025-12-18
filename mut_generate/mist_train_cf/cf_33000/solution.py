"""
QUESTION:
Implement the function `process_buffer(buf)` that takes a binary data buffer `buf` as input and extracts three sets of 6 consecutive double-precision floating-point values, storing them in a `RobotState` object's fields `q_target`, `qd_target`, and `qdd_target`, respectively. The function should return the `RobotState` object containing the extracted double values. The buffer format is as follows: the buffer contains serialized double-precision floating-point values, with each set of double values represented by 6 consecutive double-precision floating-point values. Assume that the input buffer `buf` always contains sufficient data to unpack the required number of double values for each set.
"""

import struct

class RobotState:
    def __init__(self):
        self.q_target = []
        self.qd_target = []
        self.qdd_target = []

def entrance(buf):
    rs = RobotState()
    offset = 0
    
    # Unpack and store the first set of double values in rs.q_target
    rs.q_target = list(struct.unpack_from("!dddddd", buf, offset))
    offset += 6 * 8  # Move the offset to the next set of double values
    
    # Unpack and store the second set of double values in rs.qd_target
    rs.qd_target = list(struct.unpack_from("!dddddd", buf, offset))
    offset += 6 * 8  # Move the offset to the next set of double values
    
    # Unpack and store the third set of double values in rs.qdd_target
    rs.qdd_target = list(struct.unpack_from("!dddddd", buf, offset))
    
    return rs