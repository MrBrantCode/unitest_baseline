"""
QUESTION:
Write a function `compare_epochs` that takes the batch sizes of two models, `batch_size_1` and `batch_size_2`, and the number of steps they are fine-tuned for, `steps`, as input and returns whether the model with `batch_size_1` has more, less, or the same number of epochs than the model with `batch_size_2`. Assume the sizes of the datasets are the same.
"""

def compare_epochs(batch_size_1, batch_size_2, steps):
    """
    Compare the number of epochs of two models with different batch sizes.

    Args:
    batch_size_1 (int): The batch size of the first model.
    batch_size_2 (int): The batch size of the second model.
    steps (int): The number of steps the models are fine-tuned for.

    Returns:
    str: A string indicating whether the first model has more, less, or the same number of epochs as the second model.
    """

    if batch_size_1 > batch_size_2:
        return "less"
    elif batch_size_1 < batch_size_2:
        return "more"
    else:
        return "same"