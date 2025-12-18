"""
QUESTION:
Implement a custom backpropagation function `custom_mul_add_bprop` that takes in four tensors `x`, `y`, `z`, and `dout` and returns the gradients of the `MulAdd` operation with respect to `x`, `y`, and `z`. The gradients should be computed based on the chain rule and the `MulAdd` operation's mathematical definition. The custom backpropagation function will be used in a deep learning framework to compute gradients during the backpropagation process.
"""

def custom_mul_add_bprop(x, y, z, dout):
    dx = dout * y
    dy = dout * x
    dz = dout
    return dx, dy, dz