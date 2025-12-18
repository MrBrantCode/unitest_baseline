"""
QUESTION:
Implement the `create_lr_schedule` function that generates a custom learning rate scheduler. The function should take the following parameters: 
- `initial_lr`: The initial learning rate at the start of training.
- `warmup_epochs`: The number of epochs for the warmup phase.
- `decay_rate`: The rate at which the learning rate should decay after the warmup phase.

The function should return a learning rate scheduler that adjusts the learning rate according to the specified schedule, where the learning rate increases linearly during the warmup phase and decays exponentially after the warmup phase.
"""

def create_lr_schedule(initial_lr, warmup_epochs, decay_rate):
    def lr_schedule(epoch):
        if epoch < warmup_epochs:
            return initial_lr * (epoch + 1) / warmup_epochs
        else:
            return initial_lr * decay_rate ** (epoch - warmup_epochs)

    return lr_schedule