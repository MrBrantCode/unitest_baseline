"""
QUESTION:
Implement a function named `exponential_lr_decay` that applies exponential decay to the learning rate based on the number of iterations completed. The function should take four parameters: `current_step`, `base_lr`, `decay_factor`, and `iter_timescale`, and return the updated learning rate after applying exponential decay. The function should calculate the number of timescales as the integer division of `current_step` by `iter_timescale`, and then apply the exponential decay formula `base_lr * (decay_factor ** n_timescales)`.
"""

def exponential_lr_decay(current_step, base_lr, decay_factor, iter_timescale):
    n_timescales = current_step // iter_timescale
    lr = base_lr * (decay_factor ** n_timescales)
    return lr