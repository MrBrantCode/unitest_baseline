"""
QUESTION:
Create a function named `create_scheduler` that takes three parameters: `initial_lr`, `gamma`, and `step_size`, and returns a learning rate scheduler function. This scheduler function should take an epoch as input and return the learning rate at that epoch, which is reduced by a factor of `gamma` every `step_size` epochs.
"""

def create_scheduler(initial_lr, gamma, step_size):
    def scheduler(epoch):
        return initial_lr * (gamma ** (epoch // step_size))
    return scheduler