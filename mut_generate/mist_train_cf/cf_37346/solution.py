"""
QUESTION:
Implement a function `generate_log_string` that takes in five parameters: `epoch` (the current epoch of training), `epochs` (the total number of epochs for training), `train_loss` (the loss value obtained during training), `verbose` (a boolean indicating whether verbose logging is enabled), and `metrics` (a dictionary containing additional metrics as key-value pairs). The function should return a string representing the log information. If `verbose` is `False`, return an empty string. If `verbose` is `True`, the log string should be constructed as follows: "epoch: {epoch}/{epochs} - train_loss: {train_loss:.8f} - {metric1_name}: {metric1_value} - {metric2_name}: {metric2_value} ...".
"""

def generate_log_string(epoch: int, epochs: int, train_loss: float, verbose: bool, metrics: dict) -> str:
    if not verbose:
        return ""

    log_str = f"epoch: {epoch}/{epochs} - train_loss: {train_loss:.8f}"

    if metrics:
        metric_info = " - ".join([f"{name}: {value}" for name, value in metrics.items()])
        log_str += f" - {metric_info}"

    return log_str