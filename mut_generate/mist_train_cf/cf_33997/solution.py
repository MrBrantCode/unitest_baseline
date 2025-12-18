"""
QUESTION:
Implement the `hsigmoid` function that takes input data `x`, weights `w`, labels `label`, biases `bias`, and the number of classes `num_classes` as input. The function should return the pre-output and output of the hsigmoid function based on the formula:
`pre_output = -1 * (x * w[label, :]).sum(axis=1) - bias[0, label]` and `out = 1 / (1 + np.exp(pre_output))`. The function should support batched input data and labels. The shape of `x` is `(batch_size, feature_size)`, `w` is `(num_classes - 1, feature_size)`, `label` is `(batch_size, 1)`, and `bias` is `(1, num_classes - 1)`.
"""

import numpy as np

def hsigmoid(x, w, label, bias, num_classes):
    pre_output = -1 * (x * w[label, :]).sum(axis=1) - bias[0, label]
    out = 1 / (1 + np.exp(pre_output))
    return pre_output, out